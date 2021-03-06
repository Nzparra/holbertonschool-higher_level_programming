#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
            string = string + ("#" * self.__width)
            if i != self.height - 1:
                string = string + "\n"
        return string
