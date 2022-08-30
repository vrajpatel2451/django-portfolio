from django.urls import path
from .views import getApi,getCategoriesApi,BlogView

urlpatterns = [
    path('',getApi,name="Index"),
    path('categories',getCategoriesApi,name="CatApi"),
    path('blogs',BlogView.as_view(),name="BlogApi"),
]
