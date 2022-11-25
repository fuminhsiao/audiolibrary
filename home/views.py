from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .forms import NewUserForm, UserForm, UserDetailForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.


def register_request(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful")
            return redirect("home:main")
        messages.error(request, "Unsuccessful registration, Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form":form})

def userpage(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserDetailForm(instance=request.user.userdetail)
    return render(request=request, template_name="registration/profile.html",context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
