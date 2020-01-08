#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ex = fct(*args)
    except Exception as er:
        ex = None
        print("Exception: {}".format(er), file=sys.stderr)
    else:
        return ex
