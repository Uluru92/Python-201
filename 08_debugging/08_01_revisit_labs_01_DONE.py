#Pick at least three labs and do them again while actively using a debugger.

#Revisit the labs that you had a hard time completing.
#Start them over from scratch without looking at the solution.

#Use a visual debugger, such as the one integrated in your IDE or any
#of the other options mentioned in the course to while writing the
#code for these tasks.

#This will give you a chance to revisit challenging tasks, as well as
#to train using your debugger tool.

#Pick 1: Re-Solution to exercise 02_04_reorder_numbers using a file.csv to store variables

import csv

numeros = []
contador = 1

while contador <= 10:
    try:
        numero = int(input(f"Introduce el número {contador}: "))
        numeros.append(numero)
        contador += 1
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

with open("08_debugging\dieznumeros.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(numeros)

print("\nLos 10 números fueron añadidos a 'dieznumeros.csv'.")

with open("08_debugging\dieznumeros.csv", "r") as file:
    reader = csv.reader(file)
    filas = list(reader)

ultima_fila = [int(num) for num in filas[-1]]

list_reordered = [
    ultima_fila[1], ultima_fila[3], ultima_fila[5], ultima_fila[7], ultima_fila[9],
    ultima_fila[8], ultima_fila[6], ultima_fila[4], ultima_fila[2], ultima_fila[0]
]

print("input:", ultima_fila)
print("Output:", list_reordered)
