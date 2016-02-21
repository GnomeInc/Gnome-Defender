from django.shortcuts import render, redirect, RequestContext, render_to_response
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import DataSet


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        return DataSet.objects.order_by('-date', '-time')[:5]


class DetailView(generic.DetailView):
    model = DataSet
    template_name = 'tracker/detail.html'
