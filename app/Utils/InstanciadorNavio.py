
from app.Navios.Submarino import Submarino
from app.Navios.Cruzador import Cruzador
from app.Navios.PortaAvioes import PortaAvioes
from app.Navios.Destroyer import Destroyer
from app.Navios.Encouracado import Encouracado


def instanciador_navios(classe):
    dict_classes = {
        'Submarino': Submarino(),
        'Destroyer': Destroyer(),
        'Cruzador': Cruzador(),
        'Encouracado': Encouracado(),
        'PortaAvioes': PortaAvioes()
    }

    return dict_classes[classe]