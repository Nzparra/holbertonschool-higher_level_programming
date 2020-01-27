#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """x"""
        return self.__x

    @property
    def y(self):
        """y"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of recangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format((" " * self.__x), ("#" * self.__width)))

    def __str__(self):
        """Info of rectangle"""
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        i = self.id
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(i, x, y, w, h)

    def update(self, *args, **kwargs):
        """Updates Rectangle"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """rectangle in a dictionary"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
