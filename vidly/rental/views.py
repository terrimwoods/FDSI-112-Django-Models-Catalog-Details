from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre

# Create your views here.

def home(request):
    return render(request, 'index.html', { "title": "Welcome" })

def catalog_ssr(request):
    all_movies = Movie.objects.all()
    return render(request, "catalog_ssr.html", {"title": "Catalog SSR","movies": all_movies})

def details(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "details.html", {"title": "Movie details", "movie": movie})   

def about(request):
    return render(request, 'about.html', { "title": "About me" })