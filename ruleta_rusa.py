#Ruleta rusa# 
import random;
"La computadora genera un numero aleatorio y nosotros como usuario lo tenemos que adivinar"

import random
import time

import random
import time

intento = False
def ruleta_rusa():
    tambor = [0, 0, 0, 0, 0, 1]  # 5 posiciones vacías y 1 con una bala


    input("Presiona Enter para jugar...")

    print("Girando el tambor...")
    time.sleep(2)  # Añadir una pausa para crear suspense

    bala_posicion = random.randint(0, 5)  # Posición de la bala en el tambor
    resultado = tambor[bala_posicion]

    if resultado == 0:
        print("¡Click! Suerte esta vez, ¡sigues con vida!")
    else:
        print("¡BANG! Has perdido...")

# EJECUTAR EL JUEGO EN BUCLE

respuesta = input (print('¡Bienvenido a la Ruleta Rusa!, desea jugar ? escribe si o no: '))
while (respuesta == 'si'):
    ruleta_rusa()
    respuesta = input (print('Jugar de nuevo? escribe si o no: '))
    if respuesta == 'si':
        ruleta_rusa()
    else:
          print("Hasta Pronto !")


