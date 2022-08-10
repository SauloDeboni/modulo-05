"""Módulo do teste FizzBuzz para estudo de Python."""

def multiplo(natural):
    """Módulo do teste FizzBuzz para estudo de Python."""

    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    miss = "Miss"

    # Número múltiplo de ambos imprime "FizzBuzz"
    if (int(natural) % 5 == 0) and (int(natural) % 7 == 0):
        return fizzbuzz

    # Número múltiplo de 5 imprime "Fizz"
    if int(natural) % 5 == 0:
        return fizz

    # Número múltiplo de 7 imprime "Buzz"
    if int(natural) % 7 == 0:
        return buzz

    # Outros números imprime "Miss"
    return miss
