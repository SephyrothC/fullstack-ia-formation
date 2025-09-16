import sys
import re



#Ouverture & traitement du fichier ligne par ligne--------------------------------------------
try :
    with open("fichier.txt" , "r", encoding= "utf-8") as fichier : #ouverture du fichier en lecture seul
        lecture = fichier.read()  #lecture du fichier
        lecture = lecture.lower() # minuscule
        text = lecture.replace("\n", " ").split() #remplace les saut de lignes par des espace et split les mot du text 
       # print (text) #ecriture sur le terminal
except :
    print('le fichier est introuvable')

#Séparation de ligne mot par mot ---------------------------------------------------------------
compteur_de_mot = {} # création d'un dictionnaire vierge

for mot in text : # boucle qui fait un historigramme de la répétition des mots
    compteur_de_mot[mot] = compteur_de_mot.get(mot,0)+1
#print(compteur_de_mot)

#Recherche du mot le plus commun ---------------------------------------------------------------
       
mot_le_plus_commun = None
iteration_du_mot = None
for mot,itération in compteur_de_mot.items() :    # mot est la key et itération est la value -> la boucle for parcour le dictionnaire 
    if iteration_du_mot is None or itération > iteration_du_mot : #si la value = rien ou value > value du mot dans la boucle for
        mot_le_plus_commun = mot
        iteration_du_mot = itération
print(mot_le_plus_commun, iteration_du_mot)