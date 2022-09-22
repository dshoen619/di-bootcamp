
from django.urls import path
from .views import homepage, addFilm,addDirector

urlpatterns=[
    path('homepage',homepage, name="homepage"),
    path('addFilm', addFilm, name='addFilm'),
    path('add_director',addDirector,name='add_director')

]