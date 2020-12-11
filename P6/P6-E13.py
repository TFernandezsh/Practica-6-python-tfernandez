#Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while.
#Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

#Escribe un programa que pida un número y escriba si primo o no

numero=int(input("Escribe un numero:"))

if (numero==1):

    print ("Este numero no es primo")

else:

    i=2

    while numero%i!=0:

        i+=1

    if i==numero:

        print ("Este numero es primo")

    else:

        print ("este numero no es primo")
