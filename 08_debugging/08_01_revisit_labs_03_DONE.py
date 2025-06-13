#Pick at least three labs and do them again while actively using a debugger.

#Revisit the labs that you had a hard time completing.
#Start them over from scratch without looking at the solution.

#Use a visual debugger, such as the one integrated in your IDE or any
#of the other options mentioned in the course to while writing the
#code for these tasks.

#This will give you a chance to revisit challenging tasks, as well as
#to train using your debugger tool.

#Pick 3: Re-Solution to exercise 06_lambda_sum

# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

import csv
import os

sumar = lambda a, b, c: a + b + c

num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
num3 = int(input("Ingrese el número 3: "))

resultado = sumar(num1, num2, num3)

archivo = r"08_debugging\08_01_revisit_labs_03.csv"
archivo_existe = os.path.isfile(archivo)

with open(archivo, mode='a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    if not archivo_existe:
        writer.writerow(["numero 1", "numero 2", "numero 3", "suma total"])
    
    writer.writerow([num1, num2, num3, resultado])

print(f"Los datos fueron guardados exitosamente en '{archivo}'")