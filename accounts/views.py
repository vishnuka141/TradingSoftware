from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from accounts.forms import SigninForm
from django.views.decorators.cache import cache_control

def signin_required_admin(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"you must login")
            return redirect("login")
    return wrapper


def signin_required_user(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_user:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"You must login")
            return redirect("login")
    return wrapper

class SigninView(FormView):
    template_name = 'login.html'
    form_class = SigninForm
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            pwd=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            user=authenticate(request,email=email,password=pwd)

            if user and user.is_user:
                login(request,user)
                return redirect('userhome')
            elif user and user.is_admin:
                login(request,user)
                return redirect('adminhome')
        messages.error(request,'Invalid Password or Email')
        return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@signin_required_user
def user_home(request):
    return render(request,'dashboard-home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@signin_required_admin
def admin_home(request):
    return render(request,'adminhome.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    logout(request)
    return redirect('login')