import sys
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# cnts4p16.uwaterloo.ca [30:00:44:50] "GET /icons/ok2-0.gif HTTP/1.0" 200 231
def count_request(fname, index, filter):
    file = open(fname,"r")
    total = file_len(fname)
    num_lines = 0
    get_request = 0
    print("Ananlyse du fichier...")
    for line in file:
        num_lines += 1
        percentage = round(100 * num_lines / total)
        sys.stdout.write('\r')
        sys.stdout.write("{}%".format(percentage))
        sys.stdout.flush()
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

def request_per_hour(fname):
    file = open(fname,"r")
    total = file_len(fname)
    num_lines = 0
    print("Ananlyse du fichier...")
    for line in file:
        num_lines += 1
        percentage = round(100 * num_lines / total)
        sys.stdout.write('\r')
        sys.stdout.write("{}%".format(percentage))
        sys.stdout.flush()
        letter  = line.split(" ")
        req = {}
        key = letter[1][1:6] 
        if key in req:
            req[key] += 1
        else:
            req[key] = 1
        
    file.close()

    return req

#get_request = count_request("data_project.txt",2,"GET")
#ok_request = count_request("data_project.txt",5,"200")
#print("\n Resultat: {}".format(ok_request))
r =  request_per_hour("data_project.txt")
print(r)
