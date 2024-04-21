from django.urls import path
from . import views  # Aynı dizin içerisinden views' import et

urlpatterns = [
    path("",views.home, name="home"),  # http://127.0.0.1:8000/
    path("home",views.home), # http://127.0.0.1:8000/home   home yazınca da default sayfa açılır uzantıya ne yazarsan
    path("movies",views.movies, name="movies"),
    path("movies/<int:id>", views.movieDetails, name="details")
]

