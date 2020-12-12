def presence_chaine(ch, ss_ch):
    """
    Renvoie la présence (valeur vrai) ou l'absence (valeur faux)
    de la sous-chaîne ss_ch dans la chaîne ch.

    ch : chaîne de caractères dans laquelle on recherche
    ss_ch : chaîne de caractères à rechercher

    Renvoie un booléen
    """
    if ch.count(ss_ch):
        return True
    return False


def extraire_ip(ch):
    """
    Renvoie sous forme de chaîne l'adresse IP contenue dans une chaîne.

    ch : chaîne de caractères dans laquelle on recherche l'adresse IP

    Renvoie une chaîne de caractères
    """
    import re
    # on extrait de la ligne l'adresse IP :
    IP = re.findall(r'\d+\.\d+\.\d+\.\d+', ch)
    # on extrait la chaine de caractère de la liste précédente :
    return IP[0]


def bloque_ip(un_fichier, une_iP):
    """
    Ajoute une adresse IP dans un fichier texte.

    un_fichier : descripteur d'un fichier texte
    une_iP : chaîne de caractères représentant l'adresse IP

    Pas de valeur de retour
    """
    un_fichier.write("{}\n".format(une_iP))
