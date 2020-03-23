class Navio:
    __posicoes = []
    __vidas = 0
    __posicoes_destruidas = []

    def __init__(self, tamanho):
        self.__set_vidas(tamanho)
        self.__tamanho = tamanho

    def __set_vidas(self, tamanho) -> None:
        self.__vidas = tamanho

    def set_posicoes(self, lista_pos) -> None:
        if self.__verificar_lista_pos(lista_pos):
            self.__posicoes = lista_pos

        else:
            raise ValueError

    def get_posicoes(self) -> list:
        return self.__posicoes

    def get_vidas(self) -> int:
        return self.__vidas

    def destruir_posicao(self, posicao) -> bool:
        if self.__verificar_posicao_destruida(posicao):
            self.__posicoes_destruidas.append(posicao)
            self.__diminuir_vida()
            return True

        return False

    def __diminuir_vida(self) -> None:
        self.__vidas -= 1

    def __verificar_posicao_destruida(self, posicao) -> bool:
        try:
            self.__posicoes_destruidas.index(posicao)
            return False

        except ValueError:
            return True

    def __verificar_lista_pos(self, lista_posicoes) -> bool:
        if len(lista_posicoes) == self.__tamanho:
            return True

        return False
