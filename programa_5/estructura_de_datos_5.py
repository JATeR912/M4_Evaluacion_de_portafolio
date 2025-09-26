#Un sistema de agenda de contactos con almacenamiento en un diccionario.

agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

agregar = input("Ingrese el nombre del contacto a agregar: ")
telefono = input("Ingrese el teléfono del contacto: ")
agregar_contacto(agregar, telefono)
print("Agenda de contactos:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")