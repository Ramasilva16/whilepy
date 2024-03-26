cont = 0
while ( cont < 3 ): #Mientras sea verdadera la condicion se va a repetir

    a = int (input("Ingresar un valor: "))
    b = int (input("Ingresar un valor: "))

    if (a>0 and b>0 or a<0 and b<0):
        print ("La cuenta dará positivo")
    else:
        if (a==0 or b==0):
            print("La cuenta da 0")
        else:
            print ("La cuenta es negativa")

    cont = cont + 1