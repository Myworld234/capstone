from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_add/', views.user_add, name='user_add'),
    path('user_account/', views.user_account, name='user_account'),
    path('user_logout/', views.user_logout, name='logout'),
    path('validate_user/', views.validate_user, name='validate_user'),
    ]