#cherche le mot  trouver et le compte
def count_nbr_mot(file, mot):
    data = open(file, "r")
    compteur = 0
    for ligne in data:
        resultat = ligne.find(mot)
        if resultat > 0:
            compteur +=1
    return compteur
    data.close()

#condition pour trouver le nombre d'un mot avec plusieur condition
def question5(file, mot, mot2,mot3):
    data = open(file, "r")
    compteur = 0
    for ligne in data:
        if (ligne.find(mot) > 0) and (ligne.find(mot2) > 0) and (ligne.find(mot3) < 0):
            compteur +=1
    return compteur
    data.close()

if __name__=='__main__':
    #question1
    print("Le nombre de total de requetes GET est {}".format(count_nbr_mot("data_project.txt","GET")))
    #question6
    print("Le nombre de requetes de types images est {}".format(count_nbr_mot("data_project.txt",".gif")))
    #question5
    print("Le nombre de requetes GET dans la journee de 30 sans les acces images est {}".format(question5("data_project.txt", "[30:", "GET", "gif")))




