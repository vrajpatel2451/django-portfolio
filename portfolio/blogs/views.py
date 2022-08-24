from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def getBlogs(request):
    blogs = BlogModel.objects.all()
    print(len(blogs))
    context = {
        "name":"Vraj",
        "surname":"Patel",
        "blogs":blogs
    }
    return render(request=request, template_name="blogs.html",context=context)