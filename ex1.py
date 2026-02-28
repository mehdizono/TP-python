

#Le programme devra demander à l’utilisateur de saisir son âge au clavie

age_str=input("entrer votre age:")


# convertir cette valeur en nombre entier

age=int(age_str)


#afficher un message clair
if(age <12):
    print("vous etes un enfant")
elif(13 < age < 17):
    print("vous etes un adolescent")
elif(18 < age < 64):
    print("vous etes un adulte")
else:
    print("vous etes un senior")