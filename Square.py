from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self,length):
        self.Length = length
        self.Width = length

    def get_area(self):
        area = self.Length * self.Length
        return area
    def get_perimeter(self):
        perimeter = self.Length *4
        return perimeter