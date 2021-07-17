from django.urls import path
from .import views

app_name = 'lawyer'

urlpattterns=[
    path('', views.index, name='index'),
    path('<int:lawyer_id>/', views.detail, name='detail'),

    # path('comment/create/lawyer/<int:lawyer_id>/', views.comment_create_lawyer),
    # path('comment/modify/lawyer/<int:lawyer_id>/', views.comment_modify_lawyer),
    # path('comment/delete/lawyer/<int:lawyer_id>/', views.commnet_delete_lawyer),
]