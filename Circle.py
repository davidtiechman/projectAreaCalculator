import math
from Shape import Shape

class Circle(Shape):
    def __init__(self,radus):
        self.Radus = radus
    def Type(self):
        return "Circle"
    def get_area(self):
        area = math.pi *  self.Radus**2
        return  area
    def get_perimeter(self):
        perieter = self.Radus * math.pi *2
        return perieter