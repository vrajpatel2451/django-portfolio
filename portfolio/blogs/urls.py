from django.urls import path
from .views import getBlogs

urlpatterns = [
    path('',getBlogs,name="Index"),
]
