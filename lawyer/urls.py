from django.urls import path
from .import views

app_name = 'lawyer'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:lawyer_id>/', views.detail, name='detail'),

    path('create/', views.lawyer_create, name='lawyer_create'),
    path('lawyer/modify/<int:free_id>/', views.lawyer_modify, name='lawyer_modify'),
    path('lawyer/delete/<int:free_id>/', views.lawyer_delete, name='lawyer_delete'),

    path('comment/create/lawyer/<int:lawyer_id>/', views.comment_create, name='comment_create'),
    path('comment/modify/lawyer/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/lawyer/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]