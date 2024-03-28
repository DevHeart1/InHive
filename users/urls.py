from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user_home'),
    path('signup/', views.signup, name='user_signup'),
]