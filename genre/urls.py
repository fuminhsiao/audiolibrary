from django.urls import path, reverse_lazy, re_path
from . import views

app_name = 'genre'

urlpatterns = [
    re_path(r'^genres/$', views.show_genres),

]