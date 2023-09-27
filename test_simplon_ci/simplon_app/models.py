from django.db import models


class Presence(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    email = models.EmailField()
    date_presence = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.prenom}"
    