import random, os, msvcrt
# ** elevado
#aleatorio = random.randint(menor, mayor)
trabajadores = ["juan pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel"
                "Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_t = []

def menu():
    print("Menu")
    print("1) Generar Sueldos aleatorios")
    print("2) Clasiciar Sueldos")
    print("3) Ver estadisticas")
    print("4) Reporte de sueldos")
    print("5) salir programa")
    print("=============================")
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc > 0 and opc < 6:
                break

        except:
            print("ERROR DEBE SER UN NUMERO")
    return opc

def generar_s():
    for x in range(len(trabajadores)):
        sueldo_aleatorio = random.randint(300000, 2500000)
        sueldo_t = trabajadores[x], sueldo_aleatorio
        sueldos_t.append(sueldo_t)

def clasificar_s():
    total=0
    print("==============================")
    print(f'\nSueldos menores a $800.000')
    print("-------------------------")
    print("Nombre Apellido| Sueldo")
    for x in range(len(sueldos_t)):
        if sueldos_t[x][1] > 0 and sueldos_t[x][1] < 800000:
            print(sueldos_t[x])
            total = total+1
    print("==============================")
    print("sueldos de 0 a 800.000: ",total)
    print("==============================")

    total = 0
    print("\nsueldos entre 800000 a : 2000000")
    print("-----------------------")
    print("Nombre Apellido| Sueldo")
    for x in range(len(sueldos_t)):
        if sueldos_t[x][1] > 800000 and sueldos_t[x][1] < 2000000:
            print(sueldos_t[x])
            total = total+1
    print("==============================")
    print("sueldos de 800.000 y 2000.000: ",total)
    print("==============================")

    total = 0
    print("\nsueldos de mas de 2000.000")
    print("-----------------------")
    print("Nombre Apellido| Sueldo")
    for x in range(len(sueldos_t)):
        if sueldos_t[x][1] > 2000000:
            print(sueldos_t[x])
            total = total+1
    print("==============================")
    print("sueldos de mas de 2000.000: ",total)
    print("==============================")
def ver_estadisticas():
    pass
def reporte_s():
    pass
def salir_p():
    datos_user = input("ingrese su nombre: ")
    rut = int(input('Ingrese su rut sin puntos, sin guion: '))
    os.system('cls')
    print('Finalizando programa...')
    print(f'Desarrollado por,{datos_user}')
    print(f'Rut: {rut}')
    print("\n >>PRESIONE TECLA PARA FINALIZAR<<")
    msvcrt.getch()
    exit()

