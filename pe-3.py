#!/usr/bin/env python
import sys, os
import optparse

def prime(n):
    counter = n - 1
    while counter > 1:
        if n % counter == 0:
            return counter
        counter-=1

    return counter


def main():

    p = optparse.OptionParser()
    p.add_option('--number', '-n')

    options, argument = p.parse_args()

    number = int(options.number)
    print(prime(number))

if __name__=="__main__":
    main()
