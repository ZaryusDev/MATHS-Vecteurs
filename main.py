import math

class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, v):
        if isinstance(v, Vector):
            return Vector(self.getX() + v.getX(), self.getY() + v.getY(), self.getZ() + v.getZ())
        else:
            raise Exception("Addition de vecteurs impossible")
    def __sub__(self, v):
        if isinstance(v, Vector):
            return Vector(self.getX() - v.getX(), self.getY() - v.getY(), self.getZ() - v.getZ())
        else:
            raise Exception("Soustraction de vecteurs impossible")

    def __mul__(self, r):
        if isinstance(r, int) or isinstance(r, float):
            return Vector(self.getX()*r, self.getY()*r, self.getZ()*r)
        else:
            raise Exception("Multiplication Impossible")
    def __str__(self):

        return "Vecteur ({}, {}, {})".format(self.getX(), self.getY(), self.getZ())

    def __neg__(self):
        return Vector(-self.getX(), -self.getY(), -self.getZ())

    def isCollinaire(self, v):
        if isinstance(v, Vector):
            return self.x * v.y == self.y * v.x and self.y * v.z == self.z == v.y
        else:
            raise Exception("Non Vecteur")

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z

x = Vector(1, 1, 1)
y = Vector(2, 2, 2)

print( x * 3 - y * 2)