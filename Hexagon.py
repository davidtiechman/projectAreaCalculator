from EquilateralTriangle import EquilateralTriangle
from Shape import Shape

class RegularHexagon(EquilateralTriangle):
    def Type(self):
        return "Reugle - Hexagon"
    def get_area(self):
        area = self.Rib**2 * (3**0.5/4)
        return  area * 6
    def get_perimeter(self):
        perimeter = self.Rib *6
        return perimeter