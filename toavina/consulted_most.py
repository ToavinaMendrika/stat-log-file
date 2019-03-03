def consulted_most(fname):
    file = open(fname,"r")
    datas = []
    singles = []
    occurence = []
    result = []
    print("Analyse du fichier...")
    for line in file:       
        letter  = line.split(" ")
        #print(agents[num_lines])
        datas.append(letter[0])
        
    for data in datas:    
        if data not in singles:
            singles.append(data)

    for single in singles:
        occurence.append({
            "domain":single,
            "count":datas.count(single)
        })

    result = sorted(occurence,key=lambda k: k['count'])

       
    
    
    file.close()
    return result[-1]