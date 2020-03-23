from app.Navios.Navio import Navio

class Mapa:
    __mapa = {}
    __letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):
        self.__criar_mapa()

    def get_mapa(self) -> dict:
        return self.__mapa

    def __criar_mapa(self) -> None:
        for letra in self.__letras:
            for i in range(1, 11):
                self.__mapa[f'{letra}{i}'] = None

    def adicionar_navio(self, navio: Navio):
        lista_pos = navio.get_posicoes()
        if self.verificar_posicao(lista_pos):
            for posicao in lista_pos:
                self.__mapa[posicao] = navio

            return True

        return False

    def verificar_posicao(self, lista_posicoes):
        for posicao_lista in lista_posicoes:
            posicao_mapa = self.__mapa[posicao_lista]
            if posicao_mapa is not None:
                return False

        return True

    def __str__(self):
        string_retorno = ''
        for letra in self.__letras:
            for i in range(1, 11):
                if self.__mapa[f'{letra}{i}'] is not None:
                    string_retorno += '@ '

                else:
                    string_retorno += '# '

            string_retorno += '\n'

        return string_retorno

if __name__ == '__main__':
    mp = Mapa()
    print(mp)