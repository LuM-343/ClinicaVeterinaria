#Asociar y recuperar archivos (fotos, PDFs, resultados) de una mascota.
#FUNCIONES
#asociar_documento(): Copia un archivo externo a la carpeta de la mascota y lo registra en su índice.
#ver_documentos(): Muestra los documentos asociados a una mascota.
#recuperar_documento(): Copia un documento ya asociado hacia otra ubicación, sin alterar el original.
import json
import shutil
import time
from pathlib import Path

MASCOTAS_FILE = "MASCOTAS.json"


def _cargar_mascotas():
    try:
        with open(MASCOTAS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _buscar_mascota(codigo_mascota):
    for m in _cargar_mascotas():
        if m["codigo_mascota"] == codigo_mascota:
            return m
    return None


def _ruta_indice(codigo_mascota):
    return Path(codigo_mascota) / "documentos" / f"documentos_{codigo_mascota}.json"


def _cargar_indice(codigo_mascota):
    try:
        with open(_ruta_indice(codigo_mascota), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _guardar_indice(codigo_mascota, indice):
    carpeta = Path(codigo_mascota) / "documentos"
    carpeta.mkdir(parents=True, exist_ok=True)
    with open(_ruta_indice(codigo_mascota), "w", encoding="utf-8") as f:
        json.dump(indice, f, indent=4, ensure_ascii=False)


def asociar_documento():
    print("\n=== ASOCIAR DOCUMENTO A MASCOTA ===")
    codigo_mascota = input("Código de la mascota: ").strip()
    mascota = _buscar_mascota(codigo_mascota)
    if not mascota:
        print(f"\n>> No se encontró mascota con el código '{codigo_mascota}'.")
        return

    ruta_origen = Path(input("Ruta completa del archivo a asociar: ").strip())
    if not ruta_origen.is_file():
        print(f"\n>> El archivo no existe o la ruta no es válida: '{ruta_origen}'")
        return

    descripcion = input("Descripción del documento (ej: Radiografía de cadera): ").strip()

    carpeta_documentos = Path(codigo_mascota) / "documentos"
    carpeta_documentos.mkdir(parents=True, exist_ok=True)

    # nombre único para no pisar archivos con el mismo nombre
    nombre_destino = f"{int(time.time())}_{ruta_origen.name}"
    ruta_destino = carpeta_documentos / nombre_destino

    shutil.copy2(ruta_origen, ruta_destino)  # copy2 preserva fecha/metadata, no altera el original

    indice = _cargar_indice(codigo_mascota)
    indice.append({
        "nombre_archivo": nombre_destino,
        "nombre_original": ruta_origen.name,
        "descripcion": descripcion,
        "fecha_asociado": time.strftime("%d-%m-%Y"),
    })
    _guardar_indice(codigo_mascota, indice)

    print(f"\n>> Documento '{ruta_origen.name}' asociado correctamente a {mascota['nombre_mascota']}.")


def ver_documentos():
    print("\n=== DOCUMENTOS DE UNA MASCOTA ===")
    codigo_mascota = input("Código de la mascota: ").strip()
    indice = _cargar_indice(codigo_mascota)
    if not indice:
        print("\n>> No hay documentos asociados a esta mascota.")
        return

    print(f"\n--- Documentos de {codigo_mascota} ---")
    for i, doc in enumerate(indice, start=1):
        print(f"{i}. {doc['nombre_original']} — {doc['descripcion']} ({doc['fecha_asociado']})")


def recuperar_documento():
    print("\n=== RECUPERAR / COPIAR DOCUMENTO ===")
    codigo_mascota = input("Código de la mascota: ").strip()
    indice = _cargar_indice(codigo_mascota)
    if not indice:
        print("\n>> No hay documentos asociados a esta mascota.")
        return

    for i, doc in enumerate(indice, start=1):
        print(f"{i}. {doc['nombre_original']} — {doc['descripcion']}")

    seleccion = input("Número del documento a recuperar: ").strip()
    try:
        doc = indice[int(seleccion) - 1]
    except (ValueError, IndexError):
        print("\n>> Selección inválida.")
        return

    origen = Path(codigo_mascota) / "documentos" / doc["nombre_archivo"]
    destino = Path(input("Ruta destino donde copiarlo: ").strip())
    shutil.copy2(origen, destino)
    print(f"\n>> Documento copiado a '{destino}' sin alterar el original.")