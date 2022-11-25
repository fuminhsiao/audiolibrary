from django.urls import path, reverse_lazy
from . import views

app_name = 'amplifiers'

urlpatterns = [
    path('', views.AmplifierListView.as_view(), name='all'),
    path('list/<int:pk>', views.AmplifierDetailView.as_view(), name='amplifier_detail'),
    path('amplifier/create', views.AmplifierCreateView.as_view(success_url=reverse_lazy('amplifier:all')), name='amplifier_create'),
    path('amplifier_picture/<int:pk>', views.stream_file, name='amplifier_picture'),

]
