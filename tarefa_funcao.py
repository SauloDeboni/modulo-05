def multiplo(natural):

    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    miss = "Miss"

    # Númeto múltiplo de ambos imprime "FizzBuzz"
    if (int(natural) % 5 == 0) and (int(natural) % 7 == 0):
        return fizzbuzz

    # Número múltiplo de 5 imprime "Fizz"
    elif int(natural) % 5 == 0:
        return fizz

    # Número múltiplo de 7 imprime "Buzz"
    elif int(natural) % 7 == 0:
        return buzz

    # Outros números imprime "Miss"
    else:
        return miss
