import matplotlib.pyplot as plt
import math

class MatrizAceroPasivo(list):
    def __init__(self):
        super().__init__()

    def cargar_barras_como_circulos_para_mostrar(self):
        fig, ax = plt.subplots()
        for barra in self:
            circ = plt.Circle(xy=(barra.xg, barra.yg), radius=barra.diametro/20, color='g', zorder=10)
            ax.add_patch(circ)


class MatrizAceroActivo(list):
    def __init__(self):
        super().__init__()

    def cargar_barras_como_circulos_para_mostrar(self):
        fig, ax = plt.subplots()
        for barra in self:
            radio_equivalente = (barra.area/math.pi)**0.5
            circ = plt.Circle(xy=(barra.xg, barra.yg), radius=radio_equivalente, color='r', zorder=20)
            ax.add_patch(circ)
