from django.urls import path
from . import views

app_name = 'musical'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('intro/', views.intro, name = 'intro'),
    path('about/', views.about, name = 'about')
]