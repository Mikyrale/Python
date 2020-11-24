#Définition des fonctions

def dico_rempli(un_dico):
    """
    """
    while True:
        nom=input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom=="":
            menu(un_dico)
            break
        age=int(input("Entrez l'âge (nombre entier !) : "))
        taille=float(input("Entrez la taille (en mètres) : "))
        un_dico[nom]=(age,taille)    

def dico_consu(un_dico):
    """
    """
    while True:
        selection=input("Entrer le nom (ou <enter> pour terminer) : ")
        if selection=="":
            menu(un_dico)
            break
        elif selection in un_dico :
            print("Nom : {} - âge : {} ans - taille : {} m.".format(selection,un_dico[selection][0],un_dico[selection][1]))
        else:
            print("***Nom iconnu !***")
            
def menu (un_dico):
    while True:
        choix=input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
        if choix=="R":
            dico_rempli(un_dico)
            break
        elif choix=="C":
            dico_consu(un_dico)
            break
        elif choix=="T":
            break
        else:
            print("Valeur incorrecte!\n")
       

        
#Programme Principal

dico_eleves={}
menu(dico_eleves)


