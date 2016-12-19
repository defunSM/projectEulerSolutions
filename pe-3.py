#!/usr/bin/env python
import sys, os
import optparse

def prime(n):
    counter = 1
    array = []
    while counter < n + 1:
        if n % counter == 0:
            array.append(counter)
        counter+=1

    return array


def main():

    p = optparse.OptionParser()
    p.add_option('--number', '-n')

    options, argument = p.parse_args()

    number = int(options.number)
    print(prime(number))

if __name__=="__main__":
    main()
