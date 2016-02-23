from django.shortcuts import render, redirect, RequestContext, render_to_response
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import DataSet, Gnome
from .forms import GnomeForm


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        return DataSet.objects.order_by('-date', '-time')[:5]


class DetailView(generic.DetailView):
    model = DataSet
    template_name = 'tracker/detail.html'


class AddGnomeView(FormView):
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
    logout(request)
    return HttpResponseRedirect('/tracker/')
