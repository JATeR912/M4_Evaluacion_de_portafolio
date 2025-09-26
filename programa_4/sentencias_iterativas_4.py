#Un generador de tablas de multiplicar o una calculadora de factoriales.

while True:
    try:
        numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
        if numero < 0:
            print("Por favor ingrese un número positivo o cero.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un número entero válido.")

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
