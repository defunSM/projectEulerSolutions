#!/usr/bin/env python
import sys, os
import optparse

def smallestmultiple(n):
    test = 12252240
    while True:
        array = []
        for i in range(1,20):
            if test % i == 0:
                array.append(True)
            else:
                array.append(False)

        if False not in array:
            return test

        test += 20





def main():

    p = optparse.OptionParser()
    p.add_option('--number', '-n')

    options, arguments = p.parse_args()

    number = options.number

    print(smallestmultiple(number))


if __name__=="__main__":
    main()
