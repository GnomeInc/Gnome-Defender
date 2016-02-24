# Django imports
from django.shortcuts import render, redirect, RequestContext, render_to_response
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

# Rest API Imports
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

# App Imports
from .models import DataSet, Gnome
from .forms import GnomeForm
from .serializers import DataSetSerializer, GnomeSerializer, UserSerializer


# Basic Model Views
class IndexView(generic.ListView):
    """
    A view for the data index.  It should get just the data points for the current day.
    """
    template_name = 'tracker/index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        return DataSet.objects.order_by('-date', '-time')[:5]


class DetailView(generic.DetailView):
    """
    Detailed view of just one data point.
    """
    model = DataSet
    template_name = 'tracker/detail.html'


class AddGnomeView(FormView):
    """
    Registers a new Gnome for action.
    """
    login_required = True
    template_name = 'tracker/add_gnome.html'
    form_class = GnomeForm
    success_url = '/tracker/'

    def form_valid(self, form):
        gnome = form.save(commit=False)
        gnome.user = User.objects.get(username=self.request.user)
        gnome.save()
        return HttpResponseRedirect(self.get_success_url())


def user_login(request):
    """
    Login request view
    :param request: the http request from the user
    :return: Returns some sort of http response depending on the client's account information.
    """
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tracker/')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print('Invalid login')
            return HttpResponse('Invalid login details')
    else:
        return render_to_response('tracker/login.html', {}, context)


@login_required
def user_logout(request):
    """
    Logs the client out
    :param request: Http Request from client
    :return: A redirect back to the main page /tracker/
    """
    logout(request)
    return HttpResponseRedirect('/tracker/')


# REST API Views
@csrf_exempt
class DataSetList(generics.ListCreateAPIView):
    """
    List All DataSets, or create a new DataSet
    """
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
