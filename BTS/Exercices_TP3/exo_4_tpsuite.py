def comparaison(des_ca,des_sal):
    compa=0
    calcul=0
    for i in range(0,len(des_ca)):
        if des_ca[i]/des_sal[i]>calcul:
            calcul= des_ca[i]/des_sal[i]
            compa=i
    return compa

t_pharm=["L'ange", "Du Parc", "L'étoile", "Du square", "Sauveur", "Provident"]
t_ca=[823245, 741221, 1875, 970009, 1475324, 1247241]
t_sal=[5, 3, 1, 3, 6, 4]

résultat=(comparaison(t_ca,t_sal))
print(résultat)
print("La pharmacie la plus rentable est",t_pharm[résultat])
