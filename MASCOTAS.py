import os
import json

def registrar(estado="Activo"):
    print("\n=== REGISTRO DE MASCOTA ===")
    codigo_mascota = input("- Código: ")
    nombre_mascota = input("- Nombre: ")
    especie_mascota = input("- Especie: ")
    raza_mascota = input("- Raza: ")
    fecha_nacimiento_mascota = input("- Fecha nacimiento (dd-mm-aaaa): ")
    dueño = input("- Nombre de dueño: ")
    telefono_dueño = input("- Teléfono de dueño: ")
    estado_mascota = estado

    try: 
        os.mkdir(codigo_mascota) # Se crea la carpeta para guardar los archivos de la mascota (con el código de la mascota como código)
    except FileExistsError:
        print("La carpeta de la mascota ya existe.")

    mascota = {
        "codigo_mascota": codigo_mascota,
        "nombre_mascota": nombre_mascota,
        "especie_mascota": especie_mascota,
        "raza_mascota": raza_mascota,
        "fecha_nacimiento_mascota": fecha_nacimiento_mascota,
        "dueño": dueño,
        "telefono_dueño": telefono_dueño,
        "estado_mascota": estado_mascota
    }

    try:
        with open("MASCOTAS.json", "r") as registro:
            mascotas = json.load(registro)

        mascotas.append(mascota)

        with open("MASCOTAS.json", "w") as registro:
            json.dump(mascotas, registro, indent=4, ensure_ascii=False)

    except (FileNotFoundError, json.JSONDecodeError):
        mascotas = []
        mascotas.append(mascota)

        with open("MASCOTAS.json", "w") as registro:
            json.dump(mascotas, registro, indent=4, ensure_ascii=False)


def mostrar_mascotas():
    print("\n=== MASCOTAS REGISTRADAS")
    with open("MASCOTAS.json", "r") as registro:
        mascotas = json.load(registro)

    for clave, valor in mascotas:
        print()