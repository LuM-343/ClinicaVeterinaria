import os
import json

# Registro de mascotas en .json
def registrar(estado="Activo"):
    print("\n=== REGISTRO DE MASCOTA ===")
    # Ingreso de datos de mascota
    codigo_mascota = input("- Código: ")
    nombre_mascota = input("- Nombre: ")
    especie_mascota = input("- Especie: ")
    raza_mascota = input("- Raza: ")
    fecha_nacimiento_mascota = input("- Fecha nacimiento (dd-mm-aaaa): ")
    dueño = input("- Nombre de dueño: ")
    telefono_dueño = input("- Teléfono de dueño: ")
    estado_mascota = estado # Estado inicial de mascota como ACTIVA

    # Manejo de errores si existe la carpeta de la mascota donde se guardarán sus diferentes archivos
    try: 
        os.mkdir(codigo_mascota) # Se crea la carpeta para guardar los archivos de la mascota (con el código de la mascota como código)
    except FileExistsError:
        print("\n>> La carpeta de la mascota ya existe.")

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

# Muestra de registro de mascotas
def mostrar_mascotas():
    print("\n=== MASCOTAS REGISTRADAS ===")

    try:
        with open("MASCOTAS.json", "r") as registro: # Lectura del archivo .json para imprimir registro
            mascotas = json.load(registro)
    except FileNotFoundError:
        print("\n>> ARCHIVO VACÍO.")

    for mascota in mascotas:
        if mascota['estado_mascota'] == 'Activo':
            print(f"\n--- {mascota['codigo_mascota']}: {mascota['nombre_mascota']} ---")
            print(f"- Especie: {mascota['especie_mascota']}")
            print(f"- Raza: {mascota['raza_mascota']}")
            print(f"- Fecha de nacimiento: {mascota['fecha_nacimiento_mascota']}")
            print(f"- Dueño: {mascota['dueño']} - Teléfono: {mascota['telefono_dueño']}")

# Búsqueda de mascotas por código
def busqueda_mascota():
    encontrado = False # Bandera para marcar estado de búsqueda de mascota (Encontrada/No Encontrada)

    print("\n=== BÚSQUEDA DE MASCOTA POR CÓDIGO ===")
    codigo_busqueda = input("Código de mascota a buscar: ") # Ingreso de código de mascota a buscar

    # Manejo de error si no existe el archivo .json antes de buscar
    try:
        with open("MASCOTAS.json", "r") as registro: # Lectura del archivo .json para buscar mascota
            mascotas = json.load(registro)

        for mascota in mascotas:
            if codigo_busqueda == mascota['codigo_mascota']:
                print(f"\n--- {mascota['codigo_mascota']}: {mascota['nombre_mascota']} ---")
                print(f"- Especie: {mascota['especie_mascota']}")
                print(f"- Raza: {mascota['raza_mascota']}")
                print(f"- Fecha de nacimiento: {mascota['fecha_nacimiento_mascota']}")
                print(f"- Dueño: {mascota['dueño']} - Teléfono: {mascota['telefono_dueño']}")
                print(f"- Estado: {mascota['estado_mascota']}")
                encontrado = True # Cambiar estado de bandera
                break

        if not encontrado: # En caso no se encuentre a la mascota por el código
            print("\n>> MASCOTA NO ENCONTRADA.")
                

    except FileNotFoundError:
        print("\n>> ARCHIVO VACÍO.")