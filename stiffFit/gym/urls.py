from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [


    path('', views.home, name="home"),
    path('trainer/', views.trainer, name="trainer"),
    path('trainee/', views.trainee, name="trainee"),
	path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]