"""
Modulo en el que vamos a implementar la logica que usaremos para los distintos conversores

"""

# Crear funciones para los distintos tipos de conversiones que vamos a realizar

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
    
    
def hexadecimal(num):
    """

    """
    # TODO anañdir mas validacion al valor ingresado

    # TODO crear un diccionario que contenga las letras y sus valores
    letras: dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    # TODO creamos una variable donde almacenaremos cada caracter con su indice que usaremos como el exponente
    conversion: enumerate = enumerate(reversed(num))

    # TODO variable que va a almacenar la el resultado de la conversion
    suma: int = 0

    # TODO variable donde vamos a almacenar el caracter alfabetico como decimal
    char_d: int= 0

    # TODO inicializamos el bucle e iteramos sobre el enumerate de nuestro numero alfanumerico
    for exp, digit in conversion:
        # TODO checkeamos que el digito actual este en el alfabeto
        if digit  in letras:
            # TODO agregamos la representacion decimal del caracter alfabetico a la variable previamente creada
            char_d = letras[digit]
            # sumamos el valor a la variable
            suma += int(char_d) * (16**int(exp))
        # TODO si el caracter se encuentra entre 0-9
        else:
            suma += int(digit) * (16**int(exp))

    return suma

"""
def character_decimal(char: str) -> int:
    checkea el caracter dado en hexadecimal y retorna su representacion en decimal
    parametros
    -> char: str => el caracter en cuestion
    match char:
        case "A":
            return 10
        case "B":
            return 11
        case "C":
            return 12
        case "D":
            return 13
        case "E":
            return 14
        case "F":
            return 15
"""    
def decimal(num):
    ...

print(binario_a_decimal("11111001"))
print(hexadecimal("2F8"))
print(hexadecimal("2E6"))
