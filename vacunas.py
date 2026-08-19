import csv
#Funciones
#agregarVacuna(codigo): Agrega una vacuna al archivo CSV correspondiente al código del animal.
#verVacunas(codigo): Muestra todas las vacunas registradas para el código del animal

columnas=["Vacuna", "Aplicacion", "Proxima Dosis", "Veterinario"]
def agregarVacuna(codigo):
    try:
        with open(f"{codigo}/vacuna_{codigo}.csv", 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            vacunas = list(reader)
    except FileNotFoundError:
        with open (f"{codigo}/vacuna_{codigo}.csv", 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(columnas)
            vacunas = []

    vacuna=input("Ingrese el nombre de la vacuna: ")
    fecha_aplicacion=input("Ingrese la fecha de aplicación (DD-MM-AAAA): ")
    proxima_dosis=input("Ingrese la fecha de la próxima dosis (DD-MM-AAAA): ")
    veterinario=input("Ingrese el nombre del veterinario: ")

    with open(f"{codigo}/vacuna_{codigo}.csv", 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([vacuna, fecha_aplicacion, proxima_dosis, veterinario])

def verVacunas(codigo):
    try:
        with open(f"{codigo}/vacuna_{codigo}.csv", 'r') as archivo:
            reader = csv.reader(archivo)
            vacunas = list(reader)
            if len(vacunas) <= 1:
                print("No hay registros de vacunas.")
                return
            print("\n==== Vacunas Registradas ====")
            for fila in vacunas[1:]:
                print(f"Vacuna: {fila[0]}, Fecha de Aplicación: {fila[1]}, Próxima Dosis: {fila[2]}, Veterinario: {fila[3]}")
    except FileNotFoundError:
        print("No hay vacunas registradas.")
