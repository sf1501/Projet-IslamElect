from django.db import models

class Promos(models.Model):
    name = models.CharField(max_length=100)
    image_Produit = models.ImageField(upload_to='PromosProduitImages', blank=True, null=True)
    image_Text  = models.ImageField(upload_to='PromosTextImages', blank=True, null=True)
    affichage = models.BooleanField()
    def __str__(self):
        return self.name

class New_Product(models.Model):
    name = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    affichage = models.BooleanField()
    image_Produit = models.ImageField(upload_to='PromosNewProduitImages', blank=True, null=True)

    def __str__(self):
        return "{} {} ".format(self.name,self.categorie)
class produit(models.Model):
    name = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    quantite = models.IntegerField()
    unite_quantite = models.CharField(max_length=10)
    categorie = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    specification = models.TextField(max_length=20)
    dimension = models.CharField(max_length=50,default="longueur * largeur * hauteur en cm")
    ficheTechnique = models.FileField(upload_to="FicheTechnique",blank=True,null=True)
    image = models.ImageField(upload_to='ProduitImages', blank=True, null=True)
    n_etage = models.IntegerField()
    produit_Similaire1 = models.CharField(max_length=100)
    produit_Similaire2 = models.CharField(max_length=100)
    produit_Similaire3 = models.CharField(max_length=100)

    def __str__(self):
        return "{} {} {}".format(self.name,self.mark,self.categorie)

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CategorieImages',blank=True,null=True)

    def __str__(self):
        return self.name
class Abonnee(models.Model):
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.email


