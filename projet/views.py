from django.shortcuts import render, get_object_or_404, redirect

from projet.models import Categorie, produit,Promos,New_Product,Abonnee


def show_home(request):

    if request.method == "POST":
        mail = request.POST.get("input_mail")
        if mail != None :
            Abonnee.objects.create(email=mail)

        nameP = request.POST.get("produit_categorie_name")
        prod = produit.objects.filter(name=nameP)
        cc = Categorie.objects.filter(name=nameP)
        if len(prod) != 0 :
            print("1")
            categorie = Categorie.objects.filter(name=prod[len(prod) - 1].categorie)
            if len(prod) != 0 :
                print("2")

                prodS1 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire1)[0]
                prodS2 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire2)[0]
                prodS3 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire3)[0]
                catalogues = Categorie.objects.all()
                # cate = Categorie.objects.filter(name=nom)
                indx = [i for i in range(len(catalogues)) if catalogues[i].name == categorie.name]
                indx = indx[0]
                liste = []

                reste = len(catalogues) - indx

                liste = catalogues[indx:]
                liste[reste: reste + indx] = catalogues[0:indx]
                catalogues = liste
                return redirect('/catalogue/categorie/{}/produit/{}'.format(prod[0].categorie,prod[0].name),context={'ps3': prodS3,'ps2': prodS2,'ps': prodS1,
                        'categories' : catalogues,'produit':prod,'categorie1':categorie,
                                                                              'noms' : [catalogues[0].name]})
            else :
                pass
        if len(cc) != 0 :
            catalogues = Categorie.objects.all()

            # cate = Categorie.objects.filter(name=nom)
            indx = [i for i in range(len(catalogues)) if catalogues[i].name == cc[0].name]
            indx = indx[0]
            liste = []

            reste = len(catalogues) - indx

            liste = catalogues[indx:]
            liste[reste: reste + indx] = catalogues[0:indx]
            catalogues = liste
            produitE1 = produit.objects.filter(n_etage=1, categorie=nameP)[0:4]
            produitE2 = produit.objects.filter(n_etage=2, categorie=nameP)[0:4]
            produitE3 = produit.objects.filter(n_etage=3, categorie=nameP)[0:4]
            return redirect('/catalogue/categorie/{}'.format(nameP), context={'categories': catalogues,
                                                              'produitE1': produitE1,
                                                              'produitE2': produitE2,
                                                              'produitE3': produitE3,
                                                                              'noms' : [catalogues[0].name]})

    promos = Promos.objects.all()
    prodN = New_Product.objects.filter(affichage="True")[0:2]
    categories = Categorie.objects.all()
    print([categories[0].name]," v")
    return render(request,'home.html',context={'promos':promos,'produits':prodN,'categories':categories,
                                               'noms' : [categories[0].name]})

def show_catalogue(request,nom):

    if request.method == "POST":
        nameP = request.POST.get("produit_categorie_name")
        prod = produit.objects.filter(name=nameP)
        cc = Categorie.objects.filter(name=nameP)
        if len(prod) != 0 :
            prod = produit.objects.filter(name = nameP)
            if len(prod) != 0 :
                categorie = Categorie.objects.filter(name=prod[len(prod) - 1].categorie)
                prodS1 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire1)[0]
                prodS2 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire2)[0]
                prodS3 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire3)[0]
                catalogues = Categorie.objects.all()
                # cate = Categorie.objects.filter(name=nom)
                indx = [i for i in range(len(catalogues)) if catalogues[i].name == nom]
                indx = indx[0]
                liste = []

                reste = len(catalogues) - indx

                liste = catalogues[indx:]
                liste[reste: reste + indx] = catalogues[0:indx]
                catalogues = liste
                return redirect('/catalogue/categorie/{}/produit/{}'.format(prod[0].categorie,prod[0].name),context={'ps3': prodS3,'ps2': prodS2,'ps': prodS1,
                        'categories' : catalogues,'produit':prod,'categorie1':categorie,
                                                                                        'noms' : [catalogues[0].name]})
            else :
                pass
        elif len(cc) != 0 :
            catalogues = Categorie.objects.all()
            # cate = Categorie.objects.filter(name=nom)
            indx = [i for i in range(len(catalogues)) if catalogues[i].name == nom]
            indx = indx[0]
            liste = []

            reste = len(catalogues) - indx

            liste = catalogues[indx:]
            liste[reste: reste + indx] = catalogues[0:indx]
            catalogues = liste
            produitE1 = produit.objects.filter(n_etage=1, categorie=nameP)[0:4]
            produitE2 = produit.objects.filter(n_etage=2, categorie=nameP)[0:4]
            produitE3 = produit.objects.filter(n_etage=3, categorie=nameP)[0:4]
            return redirect('/catalogue/categorie/{}'.format(nameP), context={'categories': catalogues,
                                                            'produitE1': produitE1,
                                                            'produitE2': produitE2,
                                                            'produitE3': produitE3,
                                                            'noms' : [catalogues[0].name]})
    catalogues =Categorie.objects.all()
    #cate = Categorie.objects.filter(name=nom)
    indx = [i  for i in range(len(catalogues)) if catalogues[i].name == nom]
    indx = indx[0]
    liste = []

    reste = len(catalogues) - indx

    liste = catalogues[indx:]
    liste[reste : reste + indx] = catalogues[0:indx]
    catalogues = liste
    # chaque etage contient 4 produit
    produitE1 = produit.objects.filter(n_etage=1,categorie=nom)[0:4]
    produitE2 = produit.objects.filter(n_etage=2,categorie=nom)[0:4]
    produitE3 = produit.objects.filter(n_etage=3,categorie=nom)[0:4]
    return render(request,'catalogue.html',context={'categories' : catalogues,
                                                    'produitE1':produitE1,
                                                    'produitE2':produitE2,
                                                    'produitE3':produitE3,
                                                    'noms' : [catalogues[0].name]})

def show_apropos(request):
    catalogues = Categorie.objects.all()
    return render(request, 'apropos.html',context={'noms' : [catalogues[0].name]})



def show_pageProduit(request,nomCategorie,nomProduit):
    if request.method == "POST":
        nameP = request.POST.get("produit_categorie_name")
        prod = produit.objects.filter(name=nameP)
        cc = Categorie.objects.filter(name=nameP)
        if len(prod) != 0 :
            prod = produit.objects.filter(name = nameP)
            if len(prod) != 0 :
                categorie = Categorie.objects.filter(name=prod[len(prod) - 1].categorie)
                prodS1 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire1)[0]
                prodS2 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire2)[0]
                prodS3 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire3)[0]
                catalogues = Categorie.objects.all()
                # cate = Categorie.objects.filter(name=nom)
                indx = [i for i in range(len(catalogues)) if catalogues[i].name == nomCategorie]
                indx = indx[0]
                liste = []

                reste = len(catalogues) - indx

                liste = catalogues[indx:]
                liste[reste: reste + indx] = catalogues[0:indx]
                catalogues = liste
                return redirect('/catalogue/categorie/{}/produit/{}'.format(prod[0].categorie,prod[0].name),context={'ps3': prodS3,'ps2': prodS2,'ps': prodS1,
                        'categories' : catalogues,'produit':prod,'categorie1':categorie,
                                                                                        'noms' : [catalogues[0].name]})
            else :
                pass
        elif len(cc) != 0:
            catalogues = Categorie.objects.all()
            # cate = Categorie.objects.filter(name=nom)
            indx = [i for i in range(len(catalogues)) if catalogues[i].name == nomCategorie]
            indx = indx[0]
            liste = []

            reste = len(catalogues) - indx

            liste = catalogues[indx:]
            liste[reste: reste + indx] = catalogues[0:indx]
            catalogues = liste
            produitE1 = produit.objects.filter(n_etage=1, categorie=nameP)[0:4]
            produitE2 = produit.objects.filter(n_etage=2, categorie=nameP)[0:4]
            produitE3 = produit.objects.filter(n_etage=3, categorie=nameP)[0:4]
            return redirect('/catalogue/categorie/{}'.format(nameP), context={'categories': catalogues,
                                                              'produitE1': produitE1,
                                                              'produitE2': produitE2,
                                                              'produitE3': produitE3,
                                                                              'noms' : [catalogues[0].name]})
    categorie = Categorie.objects.filter(name = nomCategorie)
    catalogues = Categorie.objects.all()
    # cate = Categorie.objects.filter(name=nom)
    indx = [i for i in range(len(catalogues)) if catalogues[i].name == nomCategorie]
    indx = indx[0]
    liste = []
    reste = len(catalogues) - indx
    liste = catalogues[indx:]
    liste[reste: reste + indx] = catalogues[0:indx]
    catalogues = liste
    prod = produit.objects.filter(name = nomProduit)
    prodS1 = produit.objects.filter(name = prod[len(prod)-1].produit_Similaire1)[0]
    prodS2 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire2)[0]
    prodS3 = produit.objects.filter(name=prod[len(prod) - 1].produit_Similaire3)[0]

    print("p : ",prodS1)
    print("nomProduit : ",categorie,", nomCategorie : ",prod)
    return  render(request,'PageProduit.html',context={'ps3': prodS3,'ps2': prodS2,'ps': prodS1,
        'categories' : catalogues,'prod':prod[0],'categorie1':categorie,
                                                       'noms' : [catalogues[0].name]})