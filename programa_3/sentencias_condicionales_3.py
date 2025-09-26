# Un programa que determine si un número es positivo, negativo o cero.

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        break   
    except ValueError:
        print("Error: Ingrese un número entero válido.")
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")