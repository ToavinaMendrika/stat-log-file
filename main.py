file = open("data_project.txt","r")
get_request = []
for line in file:
    letter  = line.split(" ")
    print(letter[2])
file.close()
