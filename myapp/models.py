from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Tarif(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Contact(models.Model):

    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    sujet = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):

        return self.nom