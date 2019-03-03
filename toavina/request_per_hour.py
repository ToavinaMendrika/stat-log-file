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
# fonction pour calculer nombre de requête par heure 
def request_per_hour(fname):
    """ return: nombre de requête par heur"""
    file = open(fname,"r")
    #total = file_len(fname)
    num_lines = 0
    #req = {}
    print("Ananlyse du fichier...")
    for line in file:
        num_lines += 1
        #letter  = line.split(" ")    
        #key = letter[1][1:6] 
        # print(key)
        # if key in req:
        #     req[key] += 1
        # else:
        #     req[key] = 1
        
    file.close()
