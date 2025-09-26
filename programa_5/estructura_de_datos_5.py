#Un sistema de agenda de contactos con almacenamiento en un diccionario.

agenda = {}

def agregar_contacto(nombre, telefono):
    telefono_formateado = '+' + telefono
    agenda[nombre] = telefono_formateado
    print(f"Contacto {nombre} agregado con teléfono {telefono_formateado}.")

nombre = input("Ingrese el nombre del contacto a agregar: ").strip().capitalize()

while True:
    telefono = input("Ingrese el teléfono (solo números, sin '+'): ").strip()
    if telefono.isdigit() and 8 <= len(telefono) <= 15:
        break
    print("Error: El teléfono debe contener solo números y tener entre 8 y 15 dígitos.")

agregar_contacto(nombre, telefono)

print("\nAgenda de contactos:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
