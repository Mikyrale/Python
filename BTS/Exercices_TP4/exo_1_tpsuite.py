import gestion_log

def analyse_log(nom):
    """
    Charge le fichier log depuis le fichier nom.log, puis analyse les attaques

    nom : nom du fichier contenant les attaques (sans l'extension .log)

    Valeur de retour : dictionnaire contenant les attaques
    """
    dico_attaques = {}
    fichier = open(nom+".log","r")
    data = tuple(fichier.readlines())
    for ligne in data:
        if gestion_log.presence_chaine(ligne, "Failed password for") == True:
            if gestion_log.extraire_ip(ligne) in dico_attaques:
                dico_attaques[gestion_log.extraire_ip(ligne)]+=1
            else:
                dico_attaques[gestion_log.extraire_ip(ligne)]=1
    fichier.close()
    return dico_attaques

def ban_ip(dico):
    """
    Bloque une adresse IP à l'origine de plus de cinq attaques.

    dico : dictionnaire qui permet de mettre en relation
    une adresse IP et un nombre d'attaques

    Pas de valeur de retour
    """
    interdiction = open("interdit.txt","w")
    for ip in dico:
        if dico[ip]>=5:
            gestion_log.bloque_ip(interdiction,ip)
    interdiction.close()
                                  
#Programme Principal           
les_attaques=analyse_log("messages")
for une_attaque in les_attaques:
    print("L'adresse",une_attaque,"est à l'origine de",les_attaques[une_attaque],"attaques.")
ban_ip(les_attaques)

        
    
