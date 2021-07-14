from django.urls import path
from .import views

app_name = 'tips'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tips_id>/', views.detail, name='tips_detail'),
]
