from django.conf.urls.static import static

from . import views
from django.urls import path,include
from stage import settings
urlpatterns = [
    path('',views.show_home),
    path('catalogue/categorie/<slug:nom>',views.show_catalogue),
    path('apropos/',views.show_apropos),
    path("catalogue/categorie/<slug:nomCategorie>/produit/<nomProduit>",views.show_pageProduit)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)