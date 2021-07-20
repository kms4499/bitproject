from django.urls import path
from .import views

app_name = 'free'

urlpatterns = [
    path('', views.index, name='index'), # 8000/free/
    path('<int:free_id>/', views.detail, name='detail'), #8000/free/1/

    path('create/', views.free_create, name='free_create'),
    path('free/modify/<int:free_id>/', views.free_modify, name='free_modify'),
    path('free/delete/<int:free_id>/', views.free_delete, name='free_delete'),

    path('comment/create/free/<int:free_id>/', views.comment_create_free, name='comment_create_free'),
    path('comment/modify/free/<int:comment_id>/', views.comment_modify_free, name='comment_modify_free'),
    path('comment/delete/free/<int:comment_id>/', views.comment_delete_free, name='comment_delete_free'),
]
