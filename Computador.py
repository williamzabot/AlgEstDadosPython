
class Computador:
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        print("Computador modelo {}, da cor {}, custa {} reais".format(
            self.modelo, self.cor, self.preco
        ))

    def cadastrar(self):
        pass
