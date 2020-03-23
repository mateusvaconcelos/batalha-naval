from app.Navios.Navio import Navio

class Cruzador(Navio):
    __tamanho = 3

    def __init__(self):
        super().__init__(self.__tamanho)

    def __str__(self):
        return 'Cruzador'
