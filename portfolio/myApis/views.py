
from os import name
from django.shortcuts import render,HttpResponse

from blogs.models import Category,BlogModel,Book,Person
from .serialize import CategoriesSerilizer,BlogSerilizer,BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status,permissions
from config.common_serilizer import seriliaze
from knox.auth import TokenAuthentication

# Create your views here.
def getApi(request):
    return render(request=request,template_name='index.html')


@api_view(['GET','POST'])
def getCategoriesApi(request):
    if request.method == 'POST':
        data = request.data
        print(data.get('name'))
        name = data.get('name')
        if(name is None):
            return Response(seriliaze(data='name field is required',success=False,error=True),status=status.HTTP_400_BAD_REQUEST)
        categoryS = CategoriesSerilizer(data={"name":name})
        categoryS.is_valid(raise_exception=False)
        categoryS.save()
        print(categoryS.errors)
        return Response(seriliaze(data=categoryS.data,success=True,error=False),status=status.HTTP_201_CREATED)

    categories = Category.objects.all()
    print(categories)
    blogData = CategoriesSerilizer(data=categories.values(),many=True)
    blogData.is_valid(raise_exception=False)
    blogData.save()
    return Response(seriliaze(data=blogData.data,success=True,error=False),status=status.HTTP_200_OK)




class BlogView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get(self,request,*args,**kwrgs):
        blogs = BlogModel.objects.all()
        serilizedBlogs = BlogSerilizer(data=blogs.values(),many=True)
        serilizedBlogs.is_valid(raise_exception=False)
        serilizedBlogs.save()
        return Response(seriliaze(data=serilizedBlogs.data,success=True,error=False),status=status.HTTP_200_OK)




# class Catego



# 1xx - Informative
# 2xx - Success
# 3xx - Redirection
# 4xx - Clients
# 5xx - Server