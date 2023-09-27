from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Presence
from django.db import transaction


@transaction.atomic()                
def index(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        
        if nom and prenom and telephone and email:
            presence = Presence(
                nom=nom,
                prenom=prenom,
                telephone=telephone,
                email=email
            )
            if presence:
                presence.save()
                messages.success(request,"ENREGISTREMENT REUSSI")
                return redirect("accueil")
            else:
                messages.error(request,"UNE ERREUR S'EST PRODUITE.")
                return redirect("accueil")
        else:
            messages.error(request,"VEUILLEZ BIEN RENSEIGNER LE FORMULAIRE S'IL VOUS PLAIT!")
            return redirect("accueil")
    return render(request,"simplon_app/inscription.html")

def ListePresence(request):
    if request.method=="POST":
        recherche = request.POST.get("recherche")
        if recherche is not None:
            if Presence.objects.filter(nom__icontains=recherche).exists():
                inscrit = Presence.objects.filter(nom__icontains=recherche)
                context = {
                    "inscrit":inscrit
                }
                return render(request,"simplon_app/inscrits.html",context=context)
            else:
                messages.error(request,"NOM INEXISTANT DANS LA BASE DE DONNEE")
                return redirect("presence")
        
    inscrit = Presence.objects.all().order_by('nom')
    context = {
        "inscrit":inscrit
    }
    return render(request,"simplon_app/inscrits.html",context=context)
    
