from django.urls import path
from .import views

app_name='users'

urlpatterns = [
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('lawregister/', views.LawRegisterView.as_view(), name='lawregister'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.homeview, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('recovery_id/', views.RecoveryIdView.as_view(), name='recovery_id'),
    # path('recovery/id/find/', views.ajax_find_id_view, name='ajax_id'),
]
