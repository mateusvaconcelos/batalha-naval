from app.Navios.Navio import Navio

class PortaAvioes(Navio):
    __tamanho = 5

    def __init__(self):
        super().__init__(self.__tamanho)

    def __str__(self):
        return 'PortaAvioes'
