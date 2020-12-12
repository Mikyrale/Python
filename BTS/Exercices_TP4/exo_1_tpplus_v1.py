import feedparser
import socket
import lxml.html

dico_fr = {
    "bienvenue" : "Bienvenue sur l'application de consultation de flux RSS !\n",
    "select_1" : """Que voulez vous faire ? :

(A)jouter un nouveau flux à la liste
(C)onsulter un flux
(Q)uitter\n""",
    "choix" : "Sélection : ",
    "erreur_valeur" : "Vous avez choisi une valeur incorrecte !\n",
    "flux" : ["https://www.developpez.com/index/rss",
              "https://www.april.org/fr/rss.xml",
              "https://rss.framasoft.org/",
              "https://www.laquadrature.net/fr/rss.xml"],
    "ajout" : "\nQuel flux voulez vous ajouter ? (<enter> pour retourner au menu) : ",
    "select_2" : "\nChoisir un élément dans la liste : \n",
    "select_3" : "\nQuel élément choisissez vous ? ",
    "savoir_plus" : "\nPour un savoir plus rendez vous sur le site !",
    "continuer" : "\nVoulez vous reconsulter un autre flux (Y/N)?  : "
    }

def menu(dico):
    print(dico["select_1"])
    while True:
        choix = input(dico["choix"])
        if choix == "A":
            ajout(dico)
            break
        if choix == "C":
            consultation(dico)
            break
        if choix == "Q" :
            exit(0)
        else:
            print(dico["erreur_valeur"])
        
def ajout(dico):
    while True:
        choix = input(dico["ajout"])
        if choix == "":
            menu(dico)
            break
        else:
            dico["flux"].append(choix)


def consultation(dico):
    print(dico["select_2"])
    incrementation = 0
    for flux in dico["flux"]:
        print("|",incrementation,"|",flux,"|")
        incrementation+=1
    test = True
    while test!=False:
        try:
            choix = int(input(dico["select_3"]))
            if choix<0 or choix>len(dico["flux"])-1:
                raise ValueError
            else:
                test=False
        except ValueError:
            print(dico["erreur_valeur"])
    affichage_flux(dico,choix)

def affichage_flux(dico,choix):
    fil = dico["flux"][choix]
    d = feedparser.parse(fil)
    liste=[]
    for flux in d.entries:
        liste.append(flux.title)
    incrementation = 0
    print(dico["select_2"])
    for element in liste:
        print("|",incrementation,"|",element,"|",end="\n")
        incrementation+=1
    test = True
    while test!=False:
        try:
            choix_flux = int(input(dico["select_3"]))
            if choix_flux<0 or choix_flux>len(liste)-1:
                raise ValueError
            else:
                test = False
        except ValueError:
            print(dico["erreur_valeur"])
    doc = lxml.html.fromstring(d.entries[choix_flux].description)
    text = doc.text_content()
    print("\n",text)
    print(dico["savoir_plus"])
    while True:
        selection = input(dico["continuer"])
        if selection == "N":
            menu(dico)
            break
        if selection == "Y":
            consultation(dico)
            break
        else:
            print(dico["erreur_valeur"])
    
    

#Programme Principal
print(dico_fr["bienvenue"])
menu(dico_fr)
