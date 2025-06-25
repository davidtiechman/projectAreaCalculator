from Rectangle import Rectangle

class Right_A_Triangle(Rectangle):
    def Type(self):
        return "Right-angled triangle"
    def get_area(self):
        area = self.Length * self.Width /2
        return area
    def get_perimeter(self):
        c = (self.Length**2 + self.Width**2)**0.5
        perimeter = c+ self.Width + self.Length
        return perimeter