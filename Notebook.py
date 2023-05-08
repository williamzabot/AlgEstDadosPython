from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        print("Notebook modelo {}, da cor {}, custa {} reais e o tempo de bateria é {}".format(
            self.modelo, self.cor, self.preco, self.__tempoDeBateria
        ))
