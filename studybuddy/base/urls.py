from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.Home ),
    path('room/', views.Room),

    path('room/<str:pk>/', views.Room),
   
    path('about/', views.About)


]
