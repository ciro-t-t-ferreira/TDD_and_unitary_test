from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    #OBS: o nome do teste deve iniciar com test_ e deve ser o mais descritivo e preciso possível
    def test_se_idade_recebe_13_03_2000_retorno_deve_ser_23(self):
        """
        Será utilizada a metodologia "GIVEN-WHEN-THEN", que leva em conta o contexto (given), executa a
        ação (when) a ser testada e compara ela com o resultado esperado (when)
        """
        entrada = '13/03/2000' #GIVEN (contexto)
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #WHEN (ação)

        assert resultado == esperado #THEN (desfecho)
        #O método assert é a forma de checar se o resultado do teste realmente bate com o esperado, é a igualdade dele que define se o teste passa ou não

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho '  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado #THEN

    def test_quando_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado  # THEN

    #Os markers, além de ajudarem na filtragem do teste, tem diversas funcionalidades, digite "pytest --markers" no terminal para checar a documentação
    @mark.calcula_bonus #permite filtrar o teste com mais facilidade, colocar no terminal: 'pytest -v -m calcular_bonus"
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcula_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        #O método abaixo checa se o resultado do teste é uma exception.
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then