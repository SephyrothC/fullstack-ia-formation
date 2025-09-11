def valider_salaire(heures, taux): 
    print("heures travaillées :",heures,taux)
    if heures > 40 :  #si on a travailler + de 40h
        print("heure sup")
        hnormal = heures*taux
        hsup = (heures-40.0) * (taux*0.5)  #calcule temps en heures sup * taux en heure sup
        print(hnormal , hsup)
        tg = hnormal + hsup
    else :
        print("normal")   
        tg = heures*taux 
    return tg

heures_travailler = input("heures travaillées :")
taux_horaires = input("taux horraires :")

#convertion en float
ht = float(heures_travailler)
th = float(taux_horaires)

tg = valider_salaire(ht, th)

print ("Pay" ,tg )   # ecrire le salaire


