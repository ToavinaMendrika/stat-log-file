#condition pour trouver le nombre d'un mot avec plusieur condition
def count_request_day_30(file, mot, mot2,mot3):
    data = open(file, "r")
    compteur = 0
    for ligne in data:
        if (ligne.find(mot) > 0) and (ligne.find(mot2) > 0) and (ligne.find(mot3) < 0):
            compteur +=1
    return compteur
    data.close()