#Inicializamos una variable la cual contará el número de personas ingresadas
pers = int(input("personas: "))

#Verificamos que se ejecute siempre que pers sea mayor a 0
while pers > 0:
    #Solicitamos el nombre y lo guardamos en un input
    name = input("Ingrese su nombre: ")
    #Solicitamos la edad que siempre será un entero y lo guardamos en un input
    age = int(input("Ingrese su edad en años: "))
    #Solicitamos el peso que siempre será un número flotante y lo guardamos en un input
    weight = float(input("Ingrese su peso en kg: "))
    #Solicitamos la altura que siempre será un número flotante y lo guardamos en un input
    height = float(input("Ingrese su altura en metros: "))
    #Calculamos el índice de masa corporal usando nuestra fórmula y guardamos en la variable IMC  
    IMC = weight / (height ** 2)
    #verficamos si el usuario es menor o mayor de edad
    if(age < 18):
        #Si el usuario es menor de edad, mostramos un mensaje indicando que no se puede calcular el IMC
        print("Lo siento, no se puede calcular el IMC para menores de edad.")
    elif(age >= 18):
        #Mostramos el resultado del IMC
        print(f"{name}, tu índice de masa corporal es: {IMC:.2f}")
        #Mostramos un mensaje si los datos ingresados son erroneos
    else:
        print("Favor de verificar los datos ingresados.")

        print("Ahora con los datos obtenidos, se le hará su valoración")
        #Verificamos el valor del IMC para mostrar un mensaje dependiendo del resultado
        if 0 <= IMC <= 15.99:
            print("Delgadez severa.")
        elif 16 <= IMC < 16.99:
            print("Delgadez moderada.")
        elif 17 <= IMC < 18.49:
            print("Delgadez leve.")
        elif 18.5 <= IMC < 24.99:
            print("Tienes un peso normal.")
        elif 25 <= IMC < 29.99:
            print("Tienes sobrepeso.")
        elif 30 <= IMC < 34.99:
            print("Tienes obesidad leve.")
        elif 35 <= IMC < 39.99:
            print("Tienes obesidad media.")
        elif IMC >= 40:
            print("Tienes obesidad mórbida.")