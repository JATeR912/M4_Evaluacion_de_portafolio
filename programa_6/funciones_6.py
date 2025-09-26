#Un programa que calcule el área de diferentes figuras geométricas utilizando funciones separadas.
import math

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio * radio

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) / 2) * altura

def pedir_valor_positivo(nombre):
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {nombre}: "))
            if valor <= 0:
                print("Error: El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Ingrese un número válido.")

figura = input("Ingrese la figura geométrica (cuadrado, rectángulo, círculo, triángulo, trapecio): ").strip().lower()

if figura == "cuadrado":
    lado = pedir_valor_positivo("lado del cuadrado")
    print(f"El área del cuadrado es: {area_cuadrado(lado):.3f}")

elif figura == "rectángulo" or figura == "rectangulo":
    base = pedir_valor_positivo("base del rectángulo")
    altura = pedir_valor_positivo("altura del rectángulo")
    print(f"El área del rectángulo es: {area_rectangulo(base, altura):.3f}")

elif figura == "círculo" or figura == "circulo":
    radio = pedir_valor_positivo("radio del círculo")
    print(f"El área del círculo es: {area_circulo(radio):.3f}")

elif figura == "triángulo" or figura == "triangulo":
    base = pedir_valor_positivo("base del triángulo")
    altura = pedir_valor_positivo("altura del triángulo")
    print(f"El área del triángulo es: {area_triangulo(base, altura):.3f}")

elif figura == "trapecio":
    base_mayor = pedir_valor_positivo("base mayor del trapecio")
    base_menor = pedir_valor_positivo("base menor del trapecio")
    altura = pedir_valor_positivo("altura del trapecio")
    print(f"El área del trapecio es: {area_trapecio(base_mayor, base_menor, altura):.3f}")

else:
    print("Figura no reconocida. Por favor ingrese una figura válida.")
