'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Ing. Manuel Vergel Escamilla
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))

horas_extras = float(input("Introduce tus horas extras: "))

paga = (horas + horas_extras) * coste
print("Tu paga es", paga)
