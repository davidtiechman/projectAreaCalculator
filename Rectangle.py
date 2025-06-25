from Shape import Shape
class Rectangle(Shape):
    def __init__(self,length,width):
        self.Length = length
        self.Width = width

    def get_area(self):
        area = self.Length * self.Width
        return area
    def get_perimeter(self):
        perimeter = self.Length *2 + self.Width *2
        return perimeter