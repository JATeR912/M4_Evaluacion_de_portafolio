#Un generador de tablas de multiplicar o una calculadora de factoriales.

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
if numero < 1:
    print("Por favor ingrese un número positivo.")
else:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")