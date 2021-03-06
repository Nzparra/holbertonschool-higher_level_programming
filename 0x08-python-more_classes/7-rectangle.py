#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.width

    def perimeter(self):
        if self.width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.width * 2)

    def __str__(self):
        string = ""
        if self.width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    string += str(self.print_symbol)
                except Exception:
                    string += type(self).print_symbol
            if i != self.height - 1:
                string = string + "\n"
        return string

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
