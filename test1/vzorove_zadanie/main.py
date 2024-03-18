from Line import Line
from Rectangle import Rectangle
from Objects import Objects


if __name__ == "__main__":
    l1 = Line(0, 0, 3, 4)
    print(l1.getSize())  # output 5.0
    r1 = Rectangle(-1, -1, 3, 4)
    print(r1.getSize());  # output 20.0
    r2 = Rectangle(-1, -1, -1, -1)
    print(r2.toString())  # output [0,0] - [10,10]
    print(r2);  # output 100.0
    o = Objects()
    o.addObject(l1)
    o.addObject(l1)
    o.addObject(r1)
    o.addObject(r2)
    print(o.getMax("Line").getSize())  # output 5.0
    print(o.getMax("Rectangle").getSize())  # output 100.0