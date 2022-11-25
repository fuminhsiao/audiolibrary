from django.urls import path, reverse_lazy
from . import views

app_name = 'membership'

urlpatterns = [
    path('/<int:pk>', views.MemberDetailView.as_view(), name='member_detail'),
    ]
