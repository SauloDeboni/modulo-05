import pytest
from tarefa_funcao import multiplo

class TesteMultiplo:
    def setup(self):
        pass

    def teste_multiplo_5(self):
        resultado = multiplo(10)
        assert resultado == "Fizz"

    def teste_multiplo_7(self):
        resultado = multiplo(21)
        assert resultado == "Buzz"

    def teste_multiplo_ambos(self):
        resultado = multiplo(35)
        assert resultado == "FizzBuzz"

    def teste_multiplo_nenhum(self):
        resultado = multiplo(29)
        assert resultado == "Miss"
