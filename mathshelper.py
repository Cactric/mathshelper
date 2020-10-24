#!/usr/bin/python

import math as maths

print("Welcome to mathshelper.py!")

quitting = False

def intput(Message):
    while True:
        attempt = input(Message)
        if attempt.isnumeric():
            return int(attempt)
        else:
            print("Needs to be an integer, try again")

def floatput(Message):
    while True:
        try:
            attempt = input(Message)
            return float(attempt)
        except:
            print("Needs to be a valid number (negatives and decimals are allowed)")

def quadratic():
    quadratic_quitting = False
    while not quadratic_quitting:
        print("Quadratic solver, equation in form ax² + bx + c\n\n")
        a = 0
        b = 0
        c = 0
        a = floatput("Enter a value for a: ")
        b = floatput("Enter a value for b: ")
        c = floatput("Enter a value for c: ")
        discrim = (b**2) - (4*a*c)
        if discrim < 0:
            # Lock out complex numbers.
            print("ax² + bx + c for these values of a, b and c does not result in real roots.")
        else:
            # Work out the root(s)
            root1 = (-b + maths.sqrt(discrim)) / (2*a)
            root2 = (-b - maths.sqrt(discrim)) / (2*a)
            if root1 == root2:
                print("\n1 root: x = " + str(root1))
            else:
                print("\n2 roots:\n    x = " + str(root1) + "\nand x = " + str(root2))
        input("\n Press [Enter] to return to the main menu...")
        return

while not quitting:
    print("\n"*2)
    print("Select an option:\n")
    print("1) Quadratic solver")
    print("q) Quit")
    option = input("\n\nPick an option: ")
    if option == "1":
        quadratic()
    if option == "q":
        quit()
