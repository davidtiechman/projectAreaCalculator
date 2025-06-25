# This is a sample Python script.
from Circle import Circle
from EquilateralTriangle import EquilateralTriangle
from Hexagon import RegularHexagon
from Rectangle import Rectangle
from Right_A_Triangle import Right_A_Triangle
from Square import Square

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



if __name__ == '__main__':

    a = RegularHexagon(6)
    print(a.Type())
    print(f"The area of the {a.Type()} is {a.get_area()} square {"meters"}.")
    print(f"The perimeter of the {a.Type()} is {a.get_perimeter()} square {"meters"}.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
