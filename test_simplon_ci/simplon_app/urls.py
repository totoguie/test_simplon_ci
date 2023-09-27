from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="accueil"),
    path("presence/",views.ListePresence,name="presence"),
]
