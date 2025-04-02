"""
Modulo en el que vamos a implementar la logica que usaremos para los distintos conversores

"""

# Crear funciones para los distintos tipos de conversiones que vamos a realizar

def binario_a_decimal(num):
    """
    Toma un numero y lo convierte en binario
    ej -> 10011
    primero lo revertimos (11001)
    luego creamos una variable donde almacenaremos el resultado y otra para almacenar la potencia de dos sobre la cual vamos a elevar
    por ultimo iteramos sobre todo los caracteres de nuestro binario repetido y le sumamos a nuestro resultado la respectiva potencia de dos

    imprimimos el resultado (19)
    """

    # TODO revertir el numero
    num_reversed = num[::-1]
    print(list(enumerate(num_reversed)))
    
    # TODO vamos sumandole aca las potencias de dos 
    conversion = 0

    # TODO crear exponente
    exp = 0

    # TODO iterar sobre cada uno de los caracteres de nuestro binario y sumarle esto a nuestro resultado
    for i in num_reversed:
       conversion += pow(2 if int(i) == 1 else 0 , exp) 
       exp += 1

    print(conversion)
    
    

def hexadecimal(num):
    ...

def decimal(num):
    ...

binario_a_decimal("11111001")
