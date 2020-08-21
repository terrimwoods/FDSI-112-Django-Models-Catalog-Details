from django.urls import path
from . import views

# valid routes for rental app
urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home,  name="home"),
    path('about', views.about, name="about"),
    path('catalog', views.catalog_ssr, name="catalog1"),
    path('details/<int:id>', views.details, name="details")
]
