import MASCOTAS
import VACUNAS
import DOCUMENTOS

while True:
    print('\n======== CLÍNICA VETERNIARIA "El Chucho Feliz" ========')
    print('MENÚ PRINCIPAL')
    print('0. Salir')
    print('1. Registrar mascota')
    print('2. Mostrar mascotas registradas')
    print('3. Buscar mascota por código')
    print('4. Registrar consulta para mascota')
    print('5. Consultar historial de consultas de mascota')
    print('6. Registrar vacuna')
    print('7. Consultar historial de vacunas de mascota')
    print('8. ')
    opcion = input('Opción: ')

    if opcion == '0':
        print('>> SALIENDO DEL PROGRAMA')
        break

    elif opcion == '1':
        # Registro de mascota
        MASCOTAS.registrar_mascota()

    elif opcion == '2':
        # Impresión de registro de mascotas
        MASCOTAS.mostrar_mascotas()

    elif opcion == '3':
        # Búsqueda de mascota por código
        MASCOTAS.busqueda_mascota()