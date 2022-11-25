from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html'), name='main'),
    path('register', views.register_request, name="register"),
    path('user', views.userpage, name="userprofile"),
]