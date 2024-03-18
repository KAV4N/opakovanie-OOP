from Line import Line
from Rectangle import Rectangle

class Objects:
    def __init__(self):
        self.__lsCurObjects = []

    def addObject(self, obj):
        if type(obj) == Line or type(obj) == Rectangle:
        #if type(obj) in [Line, Rectangle]:
            self.__lsCurObjects.append(obj)

    def getMax(self, toFindTest):
        toFind = None
        maxValueObj = None

        if toFindTest == "Line":
            toFind = Line
        elif toFindTest == "Rectangle":
            toFind = Rectangle

        if toFind:
            for obj in self.__lsCurObjects:
                #print(type(obj),toFind,isinstance(obj, toFind) )
                if type(obj) == toFind:
                    if maxValueObj is None or obj.getSize() > maxValueObj.getSize():
                        maxValueObj = obj

        return maxValueObj