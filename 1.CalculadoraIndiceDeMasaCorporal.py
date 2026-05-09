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
    