#!/usr/bin/env python
import sys, os


def multipleof3or5(x):

    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False


def main():

    array = []

    for i in range(0, 1000):

        if multipleof3or5(i):
            array.append(i)

    print(sum(array))

if __name__=="__main__":
    main()
