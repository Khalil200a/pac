from django.db import models

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.titre

class Prestation(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.titre

class Consulting(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.titre

class Produit(models.Model):
    titre = models.CharField(max_length=200)
    small_desc = models.TextField(max_length=200, blank=True)
    big_desc = models.TextField(max_length=1000, blank=True)
    fonc = models.TextField(max_length=10000, blank=True)
    titre_other = models.CharField(max_length=200, blank=True)
    desc_other = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)


    def __str__(self):
        return self.titre