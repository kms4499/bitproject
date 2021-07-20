from django.urls import path
from .import views

app_name = 'chatPage'

urlpatterns = [
    path('', views.index, name='index'),


   ]