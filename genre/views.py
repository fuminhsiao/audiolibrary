from django.shortcuts import render
from genre.models import Genre

# Create your views here.
def show_genres(request):
    return render(request, "genre/genres.html", {'genres': Genre.objects.all()})