from django.shortcuts import render

# Create your views here.


def ShowIndex(request):
    return render(request,'index.html')

def LoginUser(request):
    username=request.POST.get('uname')
    password=request.POST.get('upass')

    if username == 'jai' and password == 'jai123@':
        return render(request,'welcome.html')
    else:
        return render(request,'index.html',{'message':'Invalid user pls try again'})

