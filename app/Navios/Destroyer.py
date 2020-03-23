from app.Navios.Navio import Navio

class Destroyer(Navio):
    __tamanho = 2

    def __init__(self):
        super().__init__(self.__tamanho)

    def __str__(self):
        return 'Destroyer'
