print("HOLA BIENVENIDO AL EJERCICIO 13 DEL EXAMEN 1")
input("PRESIONA ENTER PARA CONTINUAR")

import os
os.system('cls' if os.name == 'nt' else 'clear')

num1= int(input("INGRESE EL NUMERO:  "))
num2=1
if num1>0:
    while num2 < num1:
        print(num2+1)