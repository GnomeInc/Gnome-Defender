"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Defender

    Copyright: GnomeInc, Some Rights Reserved
"""
# Django imports
from django.shortcuts import RequestContext, render_to_response
from django.template.loader import render_to_string
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Rest API Imports
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# App Imports
from .models import DataSet, Gnome
from .forms import GnomeForm
from .serializers import DataSetSerializer, GnomeSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# --------------------- Basic Model Views -----------------------------

class GnomeIndexView(generic.ListView):
    """
    A root view for the user to see all active gnomes.
    """
    template_name = 'tracker/gnome_index.html'
    context_object_name = 'gnome_index'

    def get_queryset(self):
        gnomes = None
        if self.request.user.is_authenticated():
            gnomes = Gnome.objects.filter(user=self.request.user)
        return gnomes


class DataIndexView(generic.DetailView):
    """
    Shows detailed view of one gnome.  It should get just the data points for the current day.
    """
    template_name = 'tracker/data_index.html'
    context_object_name = 'data_index'

    def get_queryset(self):
        return Gnome.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DataIndexView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            gnomes = Gnome.objects.filter(user=self.request.user)
            data = DataSet.objects.filter(gnome__in=gnomes)
            context['gnomes'] = gnomes
            context['data'] = data
            context['chart'] = chart(self.request.user, gnomes)
        return context


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


# ---------------------- Charting Functions ------------------------------

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


def chart(user, gnome):
    url = py.plot({
        "data": [{
            "x": [1, 2, 3],
            "y": [4, 2, 5]
        }],
        "layout": {
            "title": "hello world"
        }
    }, filname='hello world', sharing='public', auto_open=False)

    return tls.get_embed(url)


# <--------------------- REST API Views ----------------------------->
class DataSetList(generics.ListCreateAPIView):
    """
    REST: List All DataSets, or create a new DataSet
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


class DataSetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    REST: Retrieve, update, or delete a DataSet
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


class GnomeList(generics.ListCreateAPIView):
    """
    REST: List and create Gnomes
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GnomeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    REST: Retrieve, update, or delete a Gnome
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer


class UserList(generics.ListAPIView):
    """
    REST: List all users
    """
    # TODO Possibly get rid of this.
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    REST: Returns user details
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer
