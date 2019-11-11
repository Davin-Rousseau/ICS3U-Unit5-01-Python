#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Oct 2019
# This program uses user defined functions


def calculate_fahrenheit():
    # calculate temperature in fahrenheit

    # input
    input1 = input("Enter a temperature in degrees celcius: ")

    # process
    try:
        temp_celc = int(input1)
        temp_fahr = (9/5) * temp_celc + 32
        # output
        print("the temperature in degrees Fahrenheit: {}".format(temp_fahr))
    except ValueError:
        print("Invalid input")


def main():
    # this function just calls other functions

    # call functions
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
