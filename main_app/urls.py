from django.urls import path 
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name='home'),
    path('sharks/', views.SharkList.as_view(), name="shark_list"),
    path('sharks/about/', views.About.as_view(), name='about'),

]