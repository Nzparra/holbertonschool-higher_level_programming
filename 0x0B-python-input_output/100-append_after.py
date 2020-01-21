#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    val = ""
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            val += line
            if search_string in line:
                val += new_string
    with open(filename, "w", encoding="utf8") as file:
        file.write(val)
