from django.db import models


class Formation(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)
    necessity = models.IntegerField(blank=True)

    def __str__(self):
        return self.titre


class Prestation(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)
    necessity = models.IntegerField(blank=True)

    def __str__(self):
        return self.titre


class Consulting(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.titre

class Filters(models.Model):
    filter = models.CharField(max_length=200)

    def __str__(self):
        return self.filter


class Produit(models.Model):
    titre = models.CharField(max_length=200)
    small_desc = models.TextField(max_length=200, blank=True)
    big_desc = models.TextField(max_length=1000, blank=True)
    fonc = models.TextField(max_length=10000, blank=True)
    titre_other = models.CharField(max_length=200, blank=True)
    desc_other = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    image2 = models.ImageField(upload_to='users/', null=True, blank=True)
    image3 = models.ImageField(upload_to='users/', null=True, blank=True)
    image4 = models.ImageField(upload_to='users/', null=True, blank=True)
    image5 = models.ImageField(upload_to='users/', null=True, blank=True)
    image6 = models.ImageField(upload_to='users/', null=True, blank=True)
    image7 = models.ImageField(upload_to='users/', null=True, blank=True)
    image8 = models.ImageField(upload_to='users/', null=True, blank=True)
    image9 = models.ImageField(upload_to='users/', null=True, blank=True)
    image10 = models.ImageField(upload_to='users/', null=True, blank=True)
    pdf = models.FileField(upload_to='users/pdfs', null=True, blank=True)
    pdf2 = models.FileField(upload_to='users/pdfs', null=True, blank=True)
    filter = models.ForeignKey(Filters, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titre


