from django.contrib import admin

from projet.models import  Categorie, produit,Promos,New_Product,Abonnee

admin.site.register(Promos)
admin.site.register(Abonnee)
admin.site.register(New_Product)
admin.site.register(produit)
admin.site.register(Categorie)
