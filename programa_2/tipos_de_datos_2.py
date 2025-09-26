# Un formulario en consola que solicite información del usuario y la almacene en variables adecuadas.

nombre = input("Ingrese su nombre: ").strip().capitalize()
apellido = input("Ingrese su apellido: ").strip().capitalize()

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("Por favor ingrese una edad válida (número positivo).")
        elif edad > 150:
            print("Por favor ingrese una edad válida (máx 150).")
        else:
            break
    except ValueError:
        print("Error: Ingrese un número válido para la edad.")

ciudad = input("Ingrese su ciudad: ").strip()
pais = input("Ingrese su país: ").strip()

print(f"\nHola, {nombre} {apellido}. Tienes {edad} años y vives en {ciudad}, {pais}.")
