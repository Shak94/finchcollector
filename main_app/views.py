from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

# We are creating a class called Home and extending it from the View class
class Home (TemplateView):
    template_name="home.html"
# This is similar to response.send from express.
