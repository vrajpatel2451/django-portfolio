from django.shortcuts import render

from .forms import BlogForm, Categoryform
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

def addBlog(request):
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return render(request=request, template_name="addblog.html",context={'form':'blog'})
            # title = form.cleaned_data['title']
    #         # print(title)
    #     blog = Category(name=request.POST['title'])
    #     blog.save()
        print(form.errors)
        return render(request=request, template_name="addblog.html",context={'form':'no valid'})
    # form = BlogForm()
    # # print(form)
    form = Categoryform()
    return render(request=request, template_name="addblog.html",context={'form':form})