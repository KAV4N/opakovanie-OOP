import math


class Line:
    poradie = 0
    def __init__(self, zaciatokX, zaciatokY, koniecX, koniecY):
        if zaciatokX == koniecX and zaciatokY == koniecY:
            zaciatokX = 0
            zaciatokY = 0
            koniecX = 10
            koniecY = 10

        self._zaciatokX = float(zaciatokX)
        self._zaciatokY = float(zaciatokY)
        self._koniecX = float(koniecX)
        self._koniecY = float(koniecY)

        Line.poradie += 1
        self._poradie = Line.poradie

    def getSize(self):
        return math.sqrt((self._koniecX - self._zaciatokX) ** 2 + (self._koniecY - self._zaciatokY) ** 2)

    def toString(self):
        return f"[ {self._zaciatokX} , {self._zaciatokY} ] - [ {self._koniecX} , {self._koniecY} ]"

    def __str__(self):
        return f"{self.getSize()}"
