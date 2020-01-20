#!/usr/bin/python3
def add_attribute(obj, a, c):
    tes = getattr(obj, "__doc__", None)
    if tes is None:
        setattr(obj, a, c)
    else:
        raise TypeError("can't add new attribute")
