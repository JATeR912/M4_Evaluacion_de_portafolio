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

figura = input("Ingrese la figura geométrica (cuadrado, rectángulo, círculo, triángulo, trapecio): ")
if figura == "cuadrado":
    lado = float(input("Ingrese el lado del cuadrado: "))
    print(f"El área del cuadrado es: {area_cuadrado(lado)}")
elif figura == "rectángulo":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
elif figura == "círculo":
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"El área del círculo es: {area_circulo(radio)}")
elif figura == "triángulo":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print(f"El área del triángulo es: {area_triangulo(base, altura)}")
elif figura == "trapecio":
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    print(f"El área del trapecio es: {area_trapecio(base_mayor, base_menor, altura)}")
else:
    print("Figura no reconocida. Por favor ingrese una figura válida.")