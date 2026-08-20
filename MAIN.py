import json
import csv
import MASCOTAS
import VACUNAS
import CONSULTAS
import DOCUMENTOS


def mascota_existe(codigo):
    try:
        with open("MASCOTAS.json", "r", encoding="utf-8") as f:
            mascotas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    return any(m["codigo_mascota"] == codigo for m in mascotas)


def pedir_codigo_valido():
    codigo = input("Código de la mascota: ").strip()
    if not mascota_existe(codigo):
        print(f"\n>> No existe una mascota con el código '{codigo}'.")
        return None
    return codigo


def mostrar_resumen():
    print("\n=== RESUMEN GENERAL DEL SISTEMA ===")
    try:
        with open("MASCOTAS.json", "r", encoding="utf-8") as f:
            mascotas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        mascotas = []

    total_mascotas = len(mascotas)
    activas = sum(1 for m in mascotas if m.get("estado_mascota") == "Activo")
    total_consultas = 0
    total_vacunas = 0
    total_documentos = 0

    for m in mascotas:
        codigo = m["codigo_mascota"]

        try:
            with open(f"{codigo}/consulta_{codigo}.json", "r", encoding="utf-8") as f:
                total_consultas += len(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        try:
            with open(f"{codigo}/vacuna_{codigo}.csv", "r", encoding="utf-8") as f:
                filas = list(csv.reader(f))
                total_vacunas += max(0, len(filas) - 1)  # -1 por el encabezado
        except FileNotFoundError:
            pass

        try:
            with open(f"{codigo}/documentos/documentos_{codigo}.json", "r", encoding="utf-8") as f:
                total_documentos += len(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    print(f"- Mascotas registradas: {total_mascotas} (activas: {activas})")
    print(f"- Total de consultas registradas: {total_consultas}")
    print(f"- Total de vacunas registradas: {total_vacunas}")
    print(f"- Total de documentos asociados: {total_documentos}")


while True:
    print('\n======== CLÍNICA VETERINARIA "El Chucho Feliz" ========')
    print('MENÚ PRINCIPAL')
    print('0. Salir')
    print('1. Registrar mascota')
    print('2. Mostrar mascotas registradas')
    print('3. Buscar mascota por código')
    print('4. Registrar consulta para mascota')
    print('5. Consultar historial de consultas de mascota')
    print('6. Registrar vacuna')
    print('7. Consultar historial de vacunas de mascota')
    print('8. Asociar documento a mascota')
    print('9. Ver documentos de una mascota')
    print('10. Recuperar/copiar un documento')
    print('11. Mostrar resumen general del sistema')
    opcion = input('Opción: ')

    if opcion == '0':
        print('\n>> SALIENDO DEL PROGRAMA')
        break

    elif opcion == '1':
        MASCOTAS.registrar_mascota()

    elif opcion == '2':
        MASCOTAS.mostrar_mascotas()

    elif opcion == '3':
        MASCOTAS.busqueda_mascota()

    elif opcion == '4':
        codigo = pedir_codigo_valido()
        if codigo:
            CONSULTAS.registrarConsulta(codigo)

    elif opcion == '5':
        codigo = pedir_codigo_valido()
        if codigo:
            CONSULTAS.verConsultas(codigo)

    elif opcion == '6':
        codigo = pedir_codigo_valido()
        if codigo:
            VACUNAS.agregarVacuna(codigo)

    elif opcion == '7':
        codigo = pedir_codigo_valido()
        if codigo:
            VACUNAS.verVacunas(codigo)

    elif opcion == '8':
        DOCUMENTOS.asociar_documento()

    elif opcion == '9':
        DOCUMENTOS.ver_documentos()

    elif opcion == '10':
        DOCUMENTOS.recuperar_documento()

    elif opcion == '11':
        mostrar_resumen()

    else:
        print('\n>> Opción inválida, intenta de nuevo.')