#!/usr/bin/python3

import unittest
import pep8
import inspect
from models import rectangle, square, base


class test_Docs(unittest.TestCase):
    @classmethod
    def test_Class(cls):
        cls.base = inspect.getmembers(base, inspect.isfunction)
        cls.rect = inspect.getmembers(rectangle.Rectangle, inspect.isfunction)
        cls.sqr = inspect.getmembers(square.Square, inspect.isfunction)

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        models_base = style.check_files(['models/base.py'])
        models_rectangle = style.check_files(['models/rectangle.py'])
        models_square = style.check_files(['models/square.py'])
        test = style.check_files(['tests/test_models/test_style.py'])
        self.assertEqual(models_base.total_errors, 0,
                         "Found code style errors(models_base).")
        self.assertEqual(models_rectangle.total_errors, 0,
                         "Found code style errors(models_rectangle).")
        self.assertEqual(models_square.total_errors, 0,
                         "Found code style errors(models_square).")
        self.assertEqual(test.total_errors, 0,
                         "Found code style errors(tests).")

    def test_module_documentation(self):
        self.assertTrue(len(base.__doc__) > 0)
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(square.__doc__) > 0)

    def test_functions_class(self):
        for i in self.base:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.rect:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.sqr:
            self.assertTrue(len(i[1].__doc__) > 0)
