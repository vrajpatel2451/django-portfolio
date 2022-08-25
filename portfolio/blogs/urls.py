from django.urls import path
from .views import addBlog, getBlogs

urlpatterns = [
    path('',getBlogs,name="Index"),
    path('add',addBlog,name="AddBlog"),
]
