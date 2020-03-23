from app.Navios.Navio import Navio

class Encouracado(Navio):
    __tamanho = 4

    def __init__(self):
        super().__init__(self.__tamanho)

    def __str__(self):
        return 'Encouracado'
