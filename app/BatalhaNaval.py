from app.Jogador import Jogador

class BatalhaNaval:
    __lista_jogadores = []

    def __init__(self, jogador1: Jogador, jogador2: Jogador):
        self.adicionar_jogador(jogador1)
        self.adicionar_jogador(jogador2)

    def adicionar_jogador(self, jogador: Jogador):
        self.__lista_jogadores.append(jogador)

    def atirar(self, jogador: Jogador, posicao):
        if len(posicao) == 1:
            if not jogador.get_mapa().verificar_posicao(posicao):
                if not jogador.get_mapa().get_mapa()[posicao[0]].destruir_posicao(posicao[0]):
                    return False

                return True

        return False

if __name__ == '__main__':
    j1 = Jogador('teste1')
    j2 = Jogador('teste2')
    bt = BatalhaNaval(j1, j2)
    print(bt.atirar(j1, ['A1']))
    print(bt.atirar(j1, ['A2']))
    print(j1.get_mapa().get_mapa())
