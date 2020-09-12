from django.shortcuts import render
from django.http import HttpResponse
from . import models

from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
class TastListView(ListView):
    model = models.Task


class CreateTaskView(CreateView):
    model = models.Task
    fields = '__all__'
    # success_url = '/'


class UpdateTaskView(UpdateView):
    model = models.Task
    fields = '__all__'

class DeleteTaskView(DeleteView):
    model = models.Task
    success_url = '/'

