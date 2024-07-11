import random, os, msvcrt
# ** elevado
#aleatorio = random.randint(menor, mayor)
trabajadores = ["juan pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel"
                "Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def menu():
    print("Menu")
    print("1) Generar Sueldos aleatorios")
    print("2) Clasiciar Sueldos")
    print("3) Ver estadisticas")
    print("4) Reporte de sueldos")
    print("5) salir programa")
    print("=============================")

    opc = int(input("Ingrese una opcion: "))

def generar_s():
    for x in trabajadores:
        sueldo_aleatorio = random.randint(300000, 2500000)
        print(sueldo_aleatorio)
        return sueldo_aleatorio
def clasificar_s():
    pass
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

