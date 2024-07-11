import random, os, msvcrt
from fun import *
# ** elevado
#aleatorio = random.randint(menor, mayor)

# min, maximo

while True:
    opc = menu()
    if opc == 1:
        generar_s()
    elif opc == 2:
        clasificar_s()
    elif opc == 3:
        ver_estadisticas()
    elif opc == 4:
        reporte_s()
    elif opc == 5:
        salir_p()