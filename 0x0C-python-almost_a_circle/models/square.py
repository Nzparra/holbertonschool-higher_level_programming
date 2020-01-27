#!/usr/bin/python3
""" Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Square info"""
        x = self.x
        y = self.y
        i = self.id
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(i, x, y, self.width)

    def update(self, *args, **kwargs):
        """Updates square"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """square to dictionary"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
