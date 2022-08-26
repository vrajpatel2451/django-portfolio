from django.urls import path
from .views import signin,signup,signout

urlpatterns = [
    path('login',signin,name="Login"),
    path('register',signup,name="Register"),
    path('logout',signout,name="LogOut"),
]
