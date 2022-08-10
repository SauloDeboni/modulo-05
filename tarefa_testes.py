"""Módulo do teste FizzBuzz para estudo de Python."""
from tarefa_funcao import multiplo

class TesteMultiplo:
    """Módulo do teste FizzBuzz para estudo de Python."""
    def setup(self):
        """Setup"""
        pass

    def teste_multiplo_5(self):
        """Teste Múltiplo 5"""
        resultado = multiplo(10)
        assert resultado == "Fizz"

    def teste_multiplo_7(self):
        """Teste Múltiplo 7"""
        resultado = multiplo(21)
        assert resultado == "Buzz"

    def teste_multiplo_ambos(self):
        """Teste Múltiplo Ambos"""
        resultado = multiplo(35)
        assert resultado == "FizzBuzz"

    def teste_multiplo_nenhum(self):
        """Teste Múltiplo Nenhum"""
        resultado = multiplo(29)
        assert resultado == "Miss"
