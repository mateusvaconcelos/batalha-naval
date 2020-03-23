from app.Mapa import Mapa
from app.Navios.Navio import Navio
from app.Utils.GeradorListaPos import gerador_lista_pos
from app.Utils.InstanciadorNavio import instanciador_navios

class Jogador:
    __lista_navios = []

    def __init__(self, nome):
        self.set_nome(nome)
        self.set_mapa(Mapa())

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_mapa(self, mapa: Mapa) -> None:
        self.__mapa = mapa

    def get_nome(self) -> str:
        return self.__nome

    def get_mapa(self) -> Mapa:
        return self.__mapa

    def criar_navio(self, navio, pos_inicial, pos_final):
        classe = instanciador_navios(navio)
        try:
            classe.set_posicoes(gerador_lista_pos(pos_inicial, pos_final))
            self.__adicionar_navio(classe)

        except ValueError:
            return self.criar_navio(navio, input('Posicao Inicial: '), input('Posicao Final: '))

    def __adicionar_navio(self, navio: Navio):
        self.__mapa.adicionar_navio(navio)

if __name__ == '__main__':
    j1 = Jogador('a')
    j1.criar_navio('Submarino', 'A1', 'A2')
    print(j1.get_mapa().get_mapa())
