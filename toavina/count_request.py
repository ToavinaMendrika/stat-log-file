import sys
def file_len(fname):
    """
    Nombre de ligne dans le fichier

    Parameters
    ----------
    arg1 : file
        Fichier log à analyser 

    Returns
    -------
    int
        nombre de ligne
    """

    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# cnts4p16.uwaterloo.ca [30:00:44:50] "GET /icons/ok2-0.gif HTTP/1.0" 200 231
def count_request(fname, index, filter):
    """
    Summary line.

    fonction pour faire analise sur le log par fichier par critère et par filtre

    Parameters
    ----------
    arg1 : file
        Fichier log à analuser au format: cnts4p16.uwaterloo.ca [30:00:44:50] "GET /icons/ok2-0.gif HTTP/1.0" 200 231
    arg2 : int
        Index dans la ligne du log apres split() de chaque ligne eg: ligne[1] = [30:00:44:50]

    Returns
    -------
    int
        nombre d'occurence de filter dans index(colone) dans le fichier

    """
    file = open(fname,"r")
    get_request = 0
    print("Ananlyse du fichier...")
    for line in file:
        letter  = line.split(" ")
        try:
            if  letter[index][0] == '"':
                if letter[index][1:] == filter:
                    get_request +=1
            else:
                if letter[index]== filter:
                    get_request +=1

        except IndexError:
            pass
        
    file.close()

    return get_request