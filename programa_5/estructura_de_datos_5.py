#Un sistema de agenda de contactos con almacenamiento en un diccionario.
menu = {"1": "Agregar contacto", 
        "2": "Ver contactos", 
        "3": "Actualizar contacto",
        "4": "Eliminar contacto",
        "0": "Salir"}

agenda = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto a agregar: ").strip().capitalize()
    while True:
        telefono = input("Ingrese el teléfono (solo números, sin '+'): ").strip()
        if telefono.isdigit() and 8 <= len(telefono) <= 15:
            break
        print("Error: El teléfono debe contener solo números y tener entre 8 y 15 dígitos.")
    telefono_formateado = '+' + telefono
    agenda[nombre] = telefono_formateado
    print(f"Contacto {nombre} agregado con teléfono {telefono_formateado}.")
    return

def ver_contactos():    
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\nAgenda de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    return


def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ").strip().capitalize()
    if nombre in agenda:
        while True:
            nuevo_telefono = input("Ingrese el nuevo teléfono (solo números, sin '+'): ").strip()
            if nuevo_telefono.isdigit() and 8 <= len(nuevo_telefono) <= 15:
                break
            print("Error: El teléfono debe contener solo números y tener entre 8 y 15 dígitos.")
        agenda[nombre] = '+' + nuevo_telefono
        print(f"Contacto {nombre} actualizado con nuevo teléfono {agenda[nombre]}.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")
    return

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().capitalize()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado de la agenda.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")
    return

while True:
    print("\nMenú de opciones:")
    for key, value in menu.items():
        print(f"{key}. {value}")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        actualizar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor intente de nuevo.")


