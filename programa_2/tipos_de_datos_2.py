# Un formulario en consola que solicite información del usuario y la almacene en variables adecuadas.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")
pais = input("Ingrese su país: ")
print(f"Hola, {nombre} {apellido}. Tienes {edad} años y vives en {ciudad}, {pais}.")

