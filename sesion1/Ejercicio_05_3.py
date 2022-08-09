'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio6.py
Autor: Ing. Manuel Vergel Escamilla
Action: imprime capital obtenido de una inversión
'''
cantidad = int(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
