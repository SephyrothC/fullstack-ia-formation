#recupération des infos
heures_travailler = input("heures travaillées :")
taux_horaires = input("taux horraires :")

#convertion en float
ht = float(heures_travailler)
th = float(taux_horaires)

if ht > 40 :  #si on a travailler + de 40h
    print("heure sup")
    hnormal = ht*th
    hsup = (ht-40.0) * (th*0.5)  #calcule temps en heures sup * taux en heure sup
    print(hnormal , hsup)
    tg = hnormal + hsup
else :
    print("normal")   
    tg = ht*th 
print ("Pay" ,tg )   # ecrire le salaire


