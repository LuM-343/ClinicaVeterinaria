#Registrar consulta con codigo de consulta, Código de mascota, Fecha, Motivo,  Diagnóstico, Tratamiento, Costo.
#FUNCIONES
#registrarConsulta(codigo_mascota): Agrega una consulta al archivo JSON correspondiente al código de la mascota.
#verConsultas(codigo_mascota): Muestra todas las consultas registradas para el
import json
import os

def registrarConsulta(codigo_mascota):
    os.makedirs(codigo_mascota, exist_ok=True)  # por si la carpeta no existiera aún

    try:
        with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'r', encoding='utf-8') as archivo:
            consultas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        consultas = []

    codigo_consulta = input("Ingrese el código de la consulta: ")
    fecha = input("Ingrese la fecha de la consulta (DD-MM-AAAA): ")
    motivo = input("Ingrese el motivo de la consulta: ")
    diagnostico = input("Ingrese el diagnóstico: ")
    tratamiento = input("Ingrese el tratamiento: ")
    costo = float(input("Ingrese el costo de la consulta: "))

    nueva_consulta = {
        "codigo": codigo_consulta,
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "costo": costo
    }

    consultas.append(nueva_consulta)

    with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'w', encoding='utf-8') as archivo:
        json.dump(consultas, archivo, indent=4, ensure_ascii=False)

    print(f"\n>> Consulta '{codigo_consulta}' registrada correctamente.")

def verConsultas(codigo_mascota):
    try:
        with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'r', encoding='utf-8') as archivo:
            consultas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\n>> No hay consultas registradas.")
        return

    if not consultas:
        print("\n>> No hay registros de consultas.")
        return

    print("\n==== Consultas Registradas ====")
    for consulta in consultas:
        print(f"Código: {consulta['codigo']}, Fecha: {consulta['fecha']}, Motivo: {consulta['motivo']}, Diagnóstico: {consulta['diagnostico']}, Tratamiento: {consulta['tratamiento']}, Costo: Q{consulta['costo']:.2f}")