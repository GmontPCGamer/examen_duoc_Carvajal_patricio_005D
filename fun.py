import random, os, msvcrt, csv
# ** elevado
#aleatorio = random.randint(menor, mayor)
trabajadores = ["juan pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel"
                "Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_t = []
total_s=[]
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
        afp = sueldo_aleatorio * 0.12
        salud = sueldo_aleatorio * 0.07
        liquido = sueldo_aleatorio-afp-salud
        sueldo_t = trabajadores[x], sueldo_aleatorio, salud, afp, liquido
        sueldos_t.append(sueldo_t)

def clasificar_s():
    total=0
    print("==============================")
    print(f'\nSueldos menores a $800.000')
    print("-------------------------")
    print("Nombre Apellido| Sueldo")
    for x in range(len(sueldos_t)):
        if sueldos_t[x][1] > 0 and sueldos_t[x][1] < 800000:
            print(sueldos_t[x][0], sueldos_t[x][1])
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
            print(sueldos_t[x][0], sueldos_t[x][1])
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
            print(sueldos_t[x][0], sueldos_t[x][1])
            total = total+1
    print("==============================")
    print("sueldos de mas de 2000.000: ",total)
    print("==============================")

    resultado = 0
    for x in range(len(sueldos_t)):
        total = sueldos_t[x][1]
        resultado = resultado+total
    print(f"TOTAL SUELDOS:{resultado} ")

def ver_estadisticas():
    resultado = 0
    for x in range(len(sueldos_t)):
        total = sueldos_t[x][1]
        resultado = resultado+total
    promedio = resultado/10
    sueldos_t.sort()
    print("el sueldo mas bajo es: ",sueldos_t[0][1])
    print("el sueldo mas alto es: ", sueldos_t[9][1])
    print(f"Promedio de sueldo es: {promedio}")

    for x in range(len(sueldos_t)):
        total = sueldos_t[x][1]
        resultado = total*total
def reporte_s():
    print("Nombre empleado | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido")
    for x in range(len(sueldos_t)):
        print(f"{x+1})", sueldos_t[x])
        
        with open("listado_trabajadores", "w", newline="")as archivo:
            
        
            
def salir_p():

    datos_user = input("ingrese su nombre: ")
    rut = int(input('Ingrese su rut sin puntos, sin guion: '))
    os.system('cls')
    print('Finalizando programa...')
    print(f'Desarrollado por,{datos_user}')
    print(f'Rut: {rut}')
    esperar_t()
    exit()

##############################################
    
def esperar_t():
    print("\n >>PRESIONE TECLA PARA FINALIZAR<<")
    msvcrt.getch()
def limpiar_p():
    os.system("cls")