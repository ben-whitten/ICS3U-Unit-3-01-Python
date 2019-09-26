#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can add two numbers together.


number_1 = int(input("Input the first number (Integer):"))
number_2 = int(input("Input the second number (Integer):"))
answer = (number_1 + number_2)


def main():
    print("")
    print("{0} + {1} = {2}" .format(number_1, number_2, answer))


if __name__ == "__main__":
    main()
