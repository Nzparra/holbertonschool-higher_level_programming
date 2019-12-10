#!/usr/bin/python3
def fizzbuzz():
    a = "Fizz"
    b = "Buzz"
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("{}{}".format(a, b), end=' ')
        else:
            if(i % 3 == 0):
                print("{}".format(a), end=' ')
            elif(i % 5 == 0):
                print("{}".format(b), end=' ')
            else:
                print("{:d}".format(i), end=' ')
