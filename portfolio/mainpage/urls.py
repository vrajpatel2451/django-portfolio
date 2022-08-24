from django.urls import path
from .views import getPage

urlpatterns = [
    path('',getPage,name="Index"),
]
