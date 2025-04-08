"""
Modulo en el que vamos a implementar la logica que usaremos para los distintos conversores

"""

# TODO Crear funciones para los distintos tipos de conversiones que vamos a realizar

def binario_a_decimal(num: str) -> int:
    """
    Toma un numero y lo convierte en binario
    Parametros: 
        -> num: str => el valor en binario que vamos a convertir a decimal
    ej -> 10011
    primero lo revertimos (11001)
    luego creamos una variable donde almacenaremos el resultado y otra para almacenar la potencia de dos sobre la cual vamos a elevar
    por ultimo iteramos sobre todo los caracteres de nuestro binario repetido y le sumamos a nuestro resultado la respectiva potencia de dos


    imprimimos el resultado (19)
    """
    # TODO anañdir mas validacion al valor ingresado
    if not all(c in "01" for c in num):
        raise ValueError("Entrada no válida, solo números binarios (0-1)")

    # TODO revertir el numero
    num_reversed = num[::-1]
    
    # TODO vamos sumandole aca las potencias de dos 
    conversion = 0

    # TODO crear exponente
    exp = 0

    # TODO iterar sobre cada uno de los caracteres de nuestro binario y sumarle esto a nuestro resultado
    for i in num_reversed:
       conversion += pow(2 if int(i) == 1 else 0 , exp) 
       exp += 1

    # TODO retornar valor convertido
    #return conversion

    # TODO otra forma de realizar la conversion
    return sum(int(digit) * (2**int(exp)) for exp, digit in enumerate(reversed(num)))
    
    
def hexadecimal_a_decimal(num:str):
    """
    Toma un numero hexadecimal y lo transforma en decimal
    parametros:

    -> num: str => el valor hexadecimal al cual se le va a realizar la conversion

    Ej -> 2F8 => 760
    """
    # TODO anañdir mas validacion al valor ingresado
    if not all(c in "0123456789abcdefABCDEF" for c in num):
        raise ValueError("Entrada no valida, debe ser un numero hexadecimal (A-F, 0-9)")

    # TODO crear un diccionario que contenga las letras y sus valores
    HEX_MAP: dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    # TODO variable que va a almacenar la el resultado de la conversion
    suma: int = 0

    # TODO inicializamos el bucle e iteramos sobre el enumerate de nuestro numero alfanumerico
    for exp, digit in enumerate(reversed(num)):
        digit_value = HEX_MAP.get(digit.upper(), None) or int(digit)

        # sumamos el valor a la variable
        suma += digit_value * (16**int(exp))

    return suma

def convertir_todo(num:int):
    valor_binario = int(num, 2)
    valor_hexadecimal= int(num, 16)


    return (num, valor_binario, valor_hexadecimal)
