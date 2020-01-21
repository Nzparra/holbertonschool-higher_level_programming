#!/usr/bin/python3
def pascal_triangle(n):
    new = []
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                temp.append(new[i - 1][j - 1] + new[i - 1][j])
        new.append(temp)
    return new
