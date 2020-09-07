#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:44:49 2020

@author: mlaulin
"""

# Get user input
i = int(input("Enter 1 for converting from Fahrenheit to Celsius and  2 for converting from Celsius to Fahrenheit: "))


def f2c():
    # Ask for user input in Fahrenheit
    f = float(input("Enter the temperature in Fahrenheit: "))

    # Convert to Fahrenheit
    c = (f - 32) * 5 / 9

    return c


def c2f():
    #  Ask for user input in Celsius
    c = float(input("Enter the temperature in Celsius: "))

    # Convert to Fahrenheit
    f = (c * (9 / 5)) + 32

    return f


if i == 1:
    v = f2c()
    v = round(v, 2)
    print("The temperature in Celsius is: {}".format(v))
if i == 2:
    v = c2f()
    v = round(v, 2)
    print("The temperature in Fahrenheit is: {}".format(v))
