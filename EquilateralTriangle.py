from Shape import Shape

class EquilateralTriangle(Shape):
    def __init__(self,rib):
        self.Rib = rib
    def Type(self):
        return "Equilateral triangle"
    def get_area(self):
        area = self.Rib**2 * (3**0.5/4)
        return area
    def get_perimeter(self):
        perimeter = self.Rib * 3
        return perimeter