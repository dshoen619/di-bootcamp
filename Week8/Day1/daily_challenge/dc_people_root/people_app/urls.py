from django.urls import path
from .views import show_people

urlpatterns = [
    path('people_app',show_people,name=show_people),
]