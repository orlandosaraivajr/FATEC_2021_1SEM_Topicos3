class PrimeiraClasse:
    pass

class SegundaClasse:
    def metodo1(self):
        self.nome = ''
        self.idade = ''

obj1 = PrimeiraClasse
obj2 = SegundaClasse

''' Primeiro contato com construtor '''
class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 

    def voce_daqui_5_anos(self): 
        return self.idade + 5 

''' Segundo contato com construtor: valores padrões '''
class Pessoa: 
    def __init__(self, nome, idade=18): 
        self.nome = nome 
        self.idade = idade 

    def voce_daqui_5_anos(self): 
        return self.idade + 5 

