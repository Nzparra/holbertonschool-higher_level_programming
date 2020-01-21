#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as file:
        if (nb_lines <= 0):
            print(file.read(), end="")
        else:
            for line in file:
                if (nb_lines > 0):
                    print(line, end="")
                    nb_lines -= 1
