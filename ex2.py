def enumerate(contacts):
    i=1
    for contact in contacts:
        print(f"{i}-{contact}")
        i=i+1
    


contacts=["hamid","adi","saad","anas"]
a=0
while(a != 3):
    print("")
    print("----------MENU DU CARNET D'ADRESSE:-------------")
    print("1. Ajouter un contact à une liste")
    print("2. Afficher tous les contacts avec une numérotation")
    print("3. Quitter le programme")

    a_str=input("choisir l'operation:")
    a=int(a_str)

    if(a == 1):
        nom = input("ajouter un contact:")
        contacts.append(nom)
    elif(a == 2):
        enumerate(contacts)
    elif(a == 3):
        break
    else:
        print("entrer un valeur valid")
