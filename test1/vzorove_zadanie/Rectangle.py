from Line import Line

class Rectangle(Line):
    def __init__(self, zaciatokX, zaciatokY, koniecX, koniecY):
        super(Rectangle, self).__init__(zaciatokX, zaciatokY, koniecX, koniecY)

    def getSize(self):
        return (self._koniecX - self._zaciatokX) * (self._koniecY - self._zaciatokY)
