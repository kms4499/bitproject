from django.urls import path
from .import views

app_name='users'

urlpatterns = [
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('lawregister/', views.LawRegisterView.as_view(), name='lawregister'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('recovery/id/', views.RecoveryIdView.as_view(), name='recovery_id'),
    path('recovery/id/find/', views.ajax_find_id_view, name='ajax_id'),
    path('recovery/pw/', views.RecoveryPwView.as_view(), name='recovery_pw'),
    path('recovery/pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
    path('recovery/pw/password_reset/', views.pw_reset_view, name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
    # path('profile/post', views.profile_post_view, name='profile_post'),
    # path('profile/comment', views.profile_comment_view, name='profile_comment'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
    # path('profile/delete/', views.profile_delete_view, name='profile_delete'),
    path('user/password/', views.password_edit_view, name='password_edit'),
]
