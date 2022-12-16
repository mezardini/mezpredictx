from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('results', views.result, name="result"),
    path('logout/', views.logoutUser, name="logout")
]