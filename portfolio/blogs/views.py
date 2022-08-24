from django.shortcuts import render
from .models import BlogModel,Category

# Create your views here.
def getBlogs(request):
    blogs = BlogModel.objects.all()
    categories = Category.objects.all()
    print(len(blogs))
    context = {
        "name":"Vraj",
        "surname":"Patel",
        "blogs":blogs,
        "categories":categories
    }
    return render(request=request, template_name="blogs.html",context=context)