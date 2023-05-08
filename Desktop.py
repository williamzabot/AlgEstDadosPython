from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        print("Desktop modelo {}, da cor {}, custa {} reais e a potencia da fonte é {}".format(
            self.modelo, self.cor, self.preco, self.__potenciaDaFonte
        ))
