from toavina.count_request import *
from toavina.consulted_most import *
from daniella.question5 import *
from daniella.question6 import *
if __name__ == "__main__":
    #question 1
    get_request = count_request("data_project.txt",2,"GET")
    ok_request = count_request("data_project.txt",5,"200")
    not_found_request = count_request("data_project.txt",5,"404")
    count_request_day_30 = count_request_day_30("data_project.txt", "[30:", "GET", "gif")
    count_nbr_image = count_nbr_image("data_project.txt",".gif")
    consulted = consulted_most("data_project.txt")
    #print("\n Resultat: {}".format(ok_request))
    # r =  request_per_hour("data_project.txt")
    print("Q1: Nombre de requête GET: {}".format(get_request))
    print("Q2: \n \t - Nombre de requête reponse 200: {} \n \t - Nombre de requête reponse 404: {}".format(ok_request,not_found_request))
    print("Q5: Le nombre de requetes GET dans la journee de 30 sans les acces images est {}".format(count_request_day_30))
    print("Q6: Le nombre de requetes de types images est {}".format(count_nbr_image))
    print("Q7: L'utilisateur {} à consulter  le plus le site soit {} fois".format(consulted["domain"],consulted["count"]))