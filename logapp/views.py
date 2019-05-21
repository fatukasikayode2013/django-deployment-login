from django.shortcuts import render
from logapp.models import lmode
from logapp.forms import lform, uform
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    h = lmode.objects
    return render(request, 'home.html',{'h':h})

@login_required
def ulogout(request)    :
    logout(request)
    return HttpResponseRedirect(reverse('vhome'))

def register(request):
    registered = False
    if request.method =='POST':
        user_form = uform(data=request.POST)
        g= lform(data=request.POST)

        if user_form.is_valid() and g.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = g.save(commit=False)
            profile.user = user

            if 'pic_image' in request.FILES:
                profile.pic_image = request.FILES['pic_image']
                profile.save()
                registered =True
        else:
            print(user_form.errors, g.errors)
    else:
        user_form = uform()
        g = lform()
    return render(request, 'registeration.html',{'a':user_form,'b':g,'registered':registered})

def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('vhome'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('login fail')
            print('username: {} and password {}'.format(username,password))
            return HttpResponse('Invalid username and password')
    else:
        return render(request,'login.html')
