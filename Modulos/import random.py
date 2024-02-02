import random
intentos = 0
Numero_al_azar = random.randint(0,100)
print("Adivina el Numero")
while True:
    usuario = int(input("Intente adivinar el numero:"))
    intentos +=1
    if usuario == Numero_al_azar:
        print("¡Felicidades! Adivinaste el número en {} intentos.".format(intentos))
        break
    elif usuario < Numero_al_azar:
        print("El número es mayor a ",usuario)
    else:
        print("El número es menor a ", usuario)
        if intentos == 5:
         print("!lo siento has perdido¡")
         break
        
        
print("Fin del juego")
    




