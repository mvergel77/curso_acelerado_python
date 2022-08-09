'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio7.py
Autor: Ing. Manuel Vergel Escamilla
Action: detecta numero negativos
'''
numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Valor es menor a 0")
elif numero == 0:
    print("¡El valor es 0 !")
else:
    print("¡El valor es mayor a 0 !")
print(f"Ha escrito el número {numero}")