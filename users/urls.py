from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users_home'),
    path('signup/', views.signup, name='users_signup'),
]