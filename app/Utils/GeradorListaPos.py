
from app.Utils.ConversorLetraNumero import converter_reverso, converter


def gerador_lista_pos(pos_inicio, pos_final):

    lista_retorno = []

    if pos_inicio[0] == pos_final[0]:
        tamanho = int(pos_final[1:]) - int(pos_inicio[1:]) + 2
        for i in range(1, tamanho):
            lista_retorno.append(f'{pos_inicio[0]}{i}')

    elif pos_inicio[0] != pos_final[0]:
        tamanho = int(converter(pos_final[0])) - int(converter(pos_inicio[0])) + 2
        for i in range(1, tamanho):
            lista_retorno.append(f'{converter_reverso(i)}{pos_inicio[1:]}')

    return lista_retorno
