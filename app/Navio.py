from app.Utils.ConversorLetraNumero import Converter

class Navio:
    __navio_tamanho = {
        'PortaAvioes': 5,
        'Encouracado ': 4,
        'Cruzador': 3,
        'Destroyer': 2,
        'Submarino': 1
    }

    def __verificar_distancia(self, navio, pos_inicio, pos_final):
        distancia = pos_final - pos_inicio + 1
        if distancia != self.__navio_tamanho[navio]:
            return False

        return True

    def verificar_posicao(self, navio, pos_inicio, pos_final):
        if int(pos_inicio[1]) == int(pos_final[1]):
            if pos_inicio[0] != pos_final[0]:
                if self.__verificar_distancia(navio, Converter(pos_inicio[0]), Converter(pos_final[0])):
                    return True

            elif pos_inicio[0] == pos_final[0]:
                if self.__verificar_distancia(navio, int(pos_inicio[1]), int(pos_final[1])):
                    return True

        elif int(pos_inicio[1]) != int(pos_final[1]) and pos_inicio[0] == pos_final[0]:
            if self.__verificar_distancia(navio, int(pos_inicio[1]), int(pos_final[1])):
                return True

        return False
