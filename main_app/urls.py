from django.urls import path 
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name='home'),
    path('sharks/', views.SharkList.as_view(), name="shark_list"),
    path('sharks/about/', views.About.as_view(), name='about'),
    path('sharks/new/', views.SharkCreate.as_view(), name="shark_create"),
    path('sharks/<int:pk>/', views.SharkDetail.as_view(), name="shark_detail"),
    path('sharks/<int:pk>/update/',views.SharkUpdate.as_view(), name ="shark_update"),
    path('sharks/<int:pk>/delete/',views.SharkDelete.as_view(), name ="shark_delete"),
]
