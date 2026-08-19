import json
import shutil
import time
from pathlib import Path

BASE_DIRECTORIO = Path(".")
ARCHIVO_BD = BASE_DIRECTORIO / "base_de_datos.csv"


def cargar_datos():
    if ARCHIVO_BD.exists():
        with open(ARCHIVO_BD, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_datos(base_de_datos):
    BASE_DIRECTORIO.mkdir(exist_ok=True)
    with open(ARCHIVO_BD, "w", encoding="utf-8") as f:
        json.dump(base_de_datos, f, indent=4)

def asociar_documento(base_de_datos, base_directorio=BASE_DIRECTORIO):
    print("\nASOCIAR DOCUMENTO A MASCOTA")
    if not base_de_datos:
        print("No hay mascotas registradas. Registre una mascota primero.")
        return

    codigo_mascota = input("Ingrese el código de la mascota: ").strip().upper()

    mascota_encontrada = None
    for mascota in base_de_datos:
        if mascota.get("Codigo") == codigo_mascota:
            mascota_encontrada = mascota
            break

    if not mascota_encontrada:
        print(f"Error: No se encontró mascota con el código '{codigo_mascota}'.")
        return

    ruta_original_str = input("Ingrese la ruta completa del archivo a asociar (ej: C:\\Users\\docs\\foto.jpg): ").strip()
    ruta_original = Path(ruta_original_str)

    if not ruta_original.is_file():
        print(f"Error: El archivo no existe o la ruta no es válida: '{ruta_original}'")
        return

    descripcion = input("Ingrese una descripción para el documento (ej: Radiografía de cadera): ").strip()

    _copiar_y_registrar_documento(mascota_encontrada, ruta_original, descripcion, base_directorio)


def _copiar_y_registrar_documento(mascota, ruta_origen, descripcion, base_directorio):
    carpeta_documentos = base_directorio / mascota["Codigo"] / "documentos"
    carpeta_documentos.mkdir(exist_ok=True)

    nombre_original = ruta_origen.name
    timestamp = int(time.time())
    nombre_seguro = f"{mascota['Codigo']}_{timestamp}_{nombre_original}"
    ruta_destino = carpeta_documentos / nombre_seguro

    try:
        shutil.copy(ruta_origen, ruta_destino)

        documento_info = {
            "nombre": nombre_original,
            "ruta": str(ruta_destino.resolve()),
            "descripcion": descripcion
        }
        mascota["Documentos"].append(documento_info)
        print(f"-> Documento '{nombre_original}' asociado exitosamente.")
        return True
    except Exception as e:
        print(f"Ocurrió un error al copiar el archivo '{ruta_origen}': {e}")
        return False


def sincronizar_documentos_mascota(base_de_datos, base_directorio=BASE_DIRECTORIO):
    print("\nSINCRONIZAR DOCUMENTOS DESDE CARPETA EXTERNA")
    if not base_de_datos:
        print("No hay mascotas registradas.")
        return

    codigo_mascota = input("Ingrese el código de la mascota: ").strip().upper()
    mascota = next((m for m in base_de_datos if m.get("Codigo") == codigo_mascota), None)

    if not mascota:
        print(f"Error: No se encontró mascota con el código '{codigo_mascota}'.")
        return

    ruta_externa_str = input("Ingrese la ruta de la carpeta a sincronizar (donde tus compañeros dejan los archivos): ").strip()
    ruta_externa = Path(ruta_externa_str)

    if not ruta_externa.is_dir():
        print(f"Error: La ruta proporcionada no es una carpeta válida: '{ruta_externa}'")
        return

    print(f"Buscando nuevos archivos para '{mascota['Nombre']}' en '{ruta_externa}'...")
    archivos_asociados = 0
    for archivo_externo in ruta_externa.iterdir():
        if archivo_externo.is_file():
            respuesta = input(f"  > ¿Asociar el archivo '{archivo_externo.name}'? (s/n): ").strip().lower()
            if respuesta == 's':
                descripcion = input(f"    - Ingrese una descripción para '{archivo_externo.name}': ").strip()
                if _copiar_y_registrar_documento(mascota, archivo_externo, descripcion, base_directorio):
                    archivos_asociados += 1

    if archivos_asociados > 0:
        print(f"\nSincronización completa. Se asociaron {archivos_asociados} nuevo(s) documento(s).")
    else:
        print("\nNo se asociaron nuevos documentos.")
