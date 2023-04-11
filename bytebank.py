from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasc_quebrada = self._data_nascimento.split('/') #Split quebra a string nos pontos que tenha o caractere dado no argumento, gerando uma lista
        ano_nascimento = data_nasc_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def decrescimo_salario(self):
        if (self._salario >= 100000 and self._eh_socio()):
            self._salario = self.salario * 0.9

    def _eh_socio(self): #O underline no inicio do nome do método indica que ele deve ser utilizado apenas internamente (dentro da classe)
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self.sobrenome() in sobrenomes)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Salário excede o valor")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'