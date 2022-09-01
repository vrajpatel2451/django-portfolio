from django.urls import path
from .views import LoginView, RegisterView, getUser
from knox import views as knox_view

urlpatterns = [
    path('',getUser,name="Index"),
    path('register',RegisterView.as_view(),name="Register"),
    path('login',LoginView.as_view(),name="Login"),
    path('logout',knox_view.LogoutView.as_view(),name="logout"),
]