print("------------------CALCULATRICE:------------------")
s=0

while (s != 5):



    a_str=input("entrer le premier nombre:")
    a=int(a_str)
    b_str=input("enter le deuxieme nombre:")
    b=int(b_str)

    print("1 : addition")
    print("2 : soustraction")
    print("3 : multiplication")
    print("4 : division")
    print("5 : quitter")

    s_str = input("choisir l'operation:")
    s=int(s_str)

    if(s == 1):
        r=a+b
        print(r)
    elif(s == 2):
        r=a-b
        print(r)
    elif(s == 3):
        r=a*b
        print(r)
    elif(s == 4):
        if(b == 0):
            print("imposible de deviser sur zero")
        else:
            r=a/b
            print(r)
    elif(s == 5):
        break
    else:
        print("entrer un nombre valid")

    
