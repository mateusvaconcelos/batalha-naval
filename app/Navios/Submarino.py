from app.Navios.Navio import Navio

class Submarino(Navio):
    __tamanho = 1

    def __init__(self):
        super().__init__(self.__tamanho)

    def __str__(self):
        return 'Submarino'

if __name__ == '__main__':
    sb = Submarino()
    sb.set_posicoes(['A1'])
    print(sb.get_posicoes())
    sb.destruir_posicao(['A1'])
    print(sb.get_vidas())
