def count_nbr_image(file, mot):
    data = open(file, "r")
    compteur = 0
    for ligne in data:
        resultat = ligne.find(mot)
        if resultat > 0:
            compteur +=1
    return compteur
    data.close()