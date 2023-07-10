from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from typing import Any, Dict
from .models import Shark
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.views.generic import DetailView

# Create your views here.

# We are creating a class called Home and extending it from the View class
class Home (TemplateView):
    template_name="home.html"
# This is similar to response.send from express.
class About(TemplateView):
    template_name="about.html"


class SharkList(TemplateView):
    template_name="shark_list.html"
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data( **kwargs)
        context['sharks'] = Shark.objects.all()
        return context
    
class SharkCreate(CreateView):
    model = Shark
    fields = ['name', 'img', 'bio']
    template_name = "shark_create.html"
    success_url = "/shark/"


class SharkDetail(DetailView):
    model= Shark
    template_name ='shark_detail.html'

class SharkUpdate(UpdateView):
     model=Shark
     fields =['name', 'img','bio',]
     template_name = "shark_update.html"
     def get_success_url(self):
        return reverse ('shark_detail', kwargs ={'pk':self.object.pk})
     
class SharkDelete(DeleteView):
     model=Shark
     fields =['name', 'img','bio',]
     template_name = "shark_delete.html"
     def get_success_url(self):
        return reverse('shark_list')
     
