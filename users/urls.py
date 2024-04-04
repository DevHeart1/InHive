from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users_home'),
    path('about/', views.about, name='users_about'),
]