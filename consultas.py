#Registrar consulta con codigo de consulta, Código de mascota, Fecha, Motivo,  Diagnóstico, Tratamiento, Costo.
#FUNCIONES
#registrarConsulta(codigo_mascota): Agrega una consulta al archivo JSON correspondiente al código de la mascota.
#verConsultas(codigo_mascota): Muestra todas las consultas registradas para el
import json

def registrarConsulta(codigo_mascota):
    try:
        with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'r', encoding='utf-8') as archivo:
            consultas = json.load(archivo)
    except FileNotFoundError:
        with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'w', encoding='utf-8') as archivo:
            json.dump([], archivo)
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
        json.dump(consultas, archivo)

def verConsultas(codigo_mascota):
    try:
        with open(f"{codigo_mascota}/consulta_{codigo_mascota}.json", 'r', encoding='utf-8') as archivo:
            consultas = json.load(archivo)
            if not consultas:
                print("No hay registros de consultas.")
                return
            print("\n==== Consultas Registradas ====")
            for consulta in consultas:
                print(f"Código: {consulta['codigo']}, Fecha: {consulta['fecha']}, Motivo: {consulta['motivo']}, Diagnóstico: {consulta['diagnostico']}, Tratamiento: {consulta['tratamiento']}, Costo: Q{consulta['costo']:.2f}")
    except FileNotFoundError:
        print("No hay consultas registradas.")

registrarConsulta("0120")
verConsultas("0120")