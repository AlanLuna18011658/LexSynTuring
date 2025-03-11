"""Práctica 00 | 18011658"""

# Máquina de Turing.

def maquina_turing(data): # En esta funcion se recibe una cadena de entrada data, la cadena se convierte en una lista llamada cinta.
    cinta = list(data) # Esta parte representa una cinta de una maquina de turing.

    posicion = 0 # Variable para rastrear la posicion actual de la cabeza de la maquina de turing.
    contador_0 = 0 # Cuenta todos los simbolos 0
    contador_1 = 0 # Cuenta todos los simbolos 1
    estado_actual = 'q0' # Guarda el simbolo actual de la maquina de turing.

    while estado_actual != 'qf': # Aqui definimos la logica, el bucle while se ejecuta cuando el estado actual NO sea qf.
        simbolo = cinta[posicion] if posicion < len(cinta) else ' ' # Obtenemos el simbolo actual de la cinta en la posicion actual de la cabeza de la maquina de turing.
        #  Si no es el caso, se considera un espacio en blanco en la cinta.

        if estado_actual == 'q0' and simbolo == '0': # Estado actual q0 y simbolo 0, entonces:
            cinta[posicion] = '1' # Reemplazamos el simbolo actual de la cinta por un 1.
            posicion += 1 # Movemos la cabeza un cuadro a la derecha(right).
            estado_actual = 'q0' # El estado actual se mantiene como q0.
            contador_0 += 1 # Se incrementa el contador de 0 a 1.
        elif estado_actual == 'q0' and simbolo == '1': # Estado actual q0 y simbolo 0, entonces:
            cinta[posicion] = '0' # Reemplazamos el simbolo actual de la cinta por un 0.
            posicion += 1 # Movemos la cabeza un cuadro a la derecha(right).
            estado_actual = 'q0' # El estado actual se mantiene como q0.
            contador_1 += 1 # Se incrementa el contador de 1 en 1.
        elif estado_actual == 'q0' and simbolo == ' ': # Si el estado actual es q0 y el simbolo es un estado vacio.
            estado_actual = 'qf' # Se actualiza el estado actual a qf(estado final).
        else:
            break # Si no se cumplen las condiciones anteriores, el bucle se finaliza.

    return estado_actual == 'qf' and contador_0 == contador_1 # El programa devuelve VERDAD si el estado actual es un estado final.
# El contador 0 y 1 tienen que tener la misma cantidad de simbolos para que esta condicion sea aceptada.


print("--¡BIENVENIDO! - Máquina de Turing--\n")

data = input("CADENA >>> ") # Ingresamos una cadena de simbolos para guardarlo en la variable data.
resultado = maquina_turing(data) # Llamamos la funcion maquina_turing pasando la cadena de simbolos y posteriormente se guarda en resultado.

if resultado: # Si el resultado es verdadero, se imprime ESTADO FINAL ACEPTADO.
    print("--ESTADO FINAL ACEPTADO--")
else: # En el caso de que el resultado resultara falso, se imprime ESTADO FINAL NO ACEPTADO.
    print("**ESTADO FINAL NO ACEPTADO, VUELVA A INTENTARLO**")
