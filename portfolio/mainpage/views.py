from django.shortcuts import render,redirect

# Create your views here.
def getPage(req):
    if req.user.is_authenticated:
        return render(request=req,template_name='index.html',context={'authenticated':True,})
    else:
        return redirect('/auth/login')