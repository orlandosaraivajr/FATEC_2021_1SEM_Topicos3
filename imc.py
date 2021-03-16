class IMC:
    def __init__(self, **kwargs):
        self._validar_dados(kwargs)
        self.peso = kwargs.get('peso', 100)
        self.altura = kwargs.get('altura', 1.75)
        self.calculo()

    def _validar_dados(self, kwargs):
        peso = kwargs.get('peso', 100)
        altura = kwargs.get('altura', 1.75)
        if not isinstance(altura, (int,float)):
            raise TypeError('Altura precisa ser inteiro ou float')
        if not isinstance(peso, (int,float)):
            raise TypeError('Peso precisa ser inteiro ou float')
        if altura <= 1.0:
            raise ValueError('Altura precisa ser maior que 1 metro')
        if altura >= 2.0:
            raise ValueError('Altura precisa ser menor que 2 metros')
        if peso <= 0:
            raise ValueError('Peso precisa ser maior que zero kgs')
        if peso > 200:
            raise ValueError('Peso precisa ser até 200 Kgs')
        
    def calculo(self):
        self.imc = round(self.peso / (self.altura*self.altura), 2)

pessoa1 = IMC()
pessoa2 = IMC(peso=80, altura=1.65)
pessoa3 = IMC(altura=1.90, peso=70)
pessoa4 = IMC(altura=1.90)
