from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

app_name = 'tips'

urlpatterns = [
    path('', views.index, name='index'),
    path('tips/<int:pk>/', views.detail, name='tips_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)