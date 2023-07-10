from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from typing import Any, Dict


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