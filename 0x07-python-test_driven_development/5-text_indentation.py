#!/usr/bin/python3


def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    txt = text.strip()
    while i < len(txt):
        print(txt[i], end='')
        if txt[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == len(txt) - 1:
                break
            if txt[i + 1] == ' ':
                i = i + 1
                while txt[i] == ' ' and txt[i + 1] == ' ' and i + 1 < len(txt):
                    i = i + 1
        i = i + 1
