'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Ing. Manuel Vergel Escamilla
Action: pago de trabajador
'''
horas_s1 = float(input("Introduce tus horas de trabajo semana 1: "))
horas_s2 = float(input("Introduce tus horas de trabajo semana 2: "))
horas_s3 = float(input("Introduce tus horas de trabajo semana 3: "))
horas_s4 = float(input("Introduce tus horas de trabajo semana 4: "))

coste = float(input("Introduce lo que cobras por hora: "))


paga = (horas_s1 + horas_s2 +horas_s3+horas_s4) * coste
print("Tu paga Mensual es", paga)
