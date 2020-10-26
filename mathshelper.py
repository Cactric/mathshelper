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

def quadratic_inequality():
    quadratic_quitting = False
    while not quadratic_quitting:
        while True:
            #Determine what style of equation we want
            styles = ["1","2","3","4","q"]
            style_equations = ["ax² + bx + c > 0","ax² + bx + c < 0","ax² + bx + c ⩾ 0","ax² + bx + c ⩽ 0"]
            
            print("Pick an equation: ")
            for x in range(len(style_equations)):
                print(str(x+1) + ") " + style_equations[x])
            print("q) Quit back to main menu")
        
            style = input("Enter the equation's number: ")
            
            if styles.count(style) > 0:
                #If it’s in the list at least once, then continue
                if style == "q":
                    #Return if the user wants to go back
                    return
                style = int(style) #Convert it to an int, makes stuff easier later
                break
            else:
                print("That wasn't a valid style, try again")
        
        print("\n\n\nQuadratic inequality solver, equation in form {}\n\n".format(style_equations[style-1]))
        a = 0
        b = 0
        c = 0
        a = floatput("Enter a value for a: ")
        b = floatput("Enter a value for b: ")
        c = floatput("Enter a value for c: ")
        discrim = (b**2) - (4*a*c)
        if a == 0:
            print("For it to be a quadratic, a must not be 0.")
        if discrim <= 0:
            # Lock out complex numbers.
            # I guess the whole curve would be above or below the x axis
            if a < 0: #if it is negative
                print("The whole curve is below the x axis")
            if a > 0: #if it is positive
                print("The whole curve is above the x axis")
        else:
            # Work out the root(s)
            root1 = (-b + maths.sqrt(discrim)) / (2*a)
            root2 = (-b - maths.sqrt(discrim)) / (2*a)
            strict_signs = [">", "<"]
            equalto_signs = ["⩾","⩽"]
            
            if style == 1 or style == 3: #greater than
                if a > 0: # U shape
                    #Now the regions will be split into two
                    #⩾⩽
                    if style == 1:
                        print("x {} {} and x {} {}".format(strict_signs[0], root1, strict_signs[1], root2))
                    if style == 3:
                        print("x {} {} and x {} {}".format(equalto_signs[0], root1, equalto_signs[1], root2))
                if a < 0: # n shape
                    #The region will be in the centre
                    if style == 1:
                        print("{} {} x {} {}".format(root2, strict_signs[1], strict_signs[1], root1))
                    if style == 3:
                        print("{} {} x {} {}".format(root2, equalto_signs[1], equalto_signs[1], root1))
            
            if style == 2 or style == 4: #less than
                if a > 0: # U shape
                    #The region will be in the centre
                    #⩾⩽
                    if style == 2:
                        print("{} {} x {} {}".format(root2, strict_signs[1], strict_signs[1], root1))
                    if style == 4:
                        print("{} {} x {} {}".format(root2, equalto_signs[1], equalto_signs[1], root1))
                if a < 0: # n shape
                    #The region will be split in 2
                    if style == 2:
                        print("x {} {} and x {} {}".format(strict_signs[1], root1, strict_signs[0], root2))
                    if style == 4:
                        print("x {} {} and x {} {}".format(equalto_signs[1], root1, equalto_signs[0], root2))
                    
            
        input("\n Press [Enter] to return to the main menu...")
        return

def primefactorise():
    print("\n\nPrime factor finder")
    primefactors = []
    divisor = 2
    givenint = intput("Enter a number you want to find the prime numbers of: ")
    currentint = givenint
    if givenint <= 1:
        print("The number needs to be 2 or above since the smallest prime number is 2")
    else:
        if givenint >= 33554432:
            #Don’t leave the user hanging
            print("The number you've given is rather large and may take a while to find factors for.")
            confirm = input("Do you want to continue [Y/n]: ")
            if confirm.lower() == "y" or confirm == "":
                pass
            else:
                return
        biggestprime = givenint / 2
        while divisor <= biggestprime:
            if currentint % divisor == 0: #If currentint is a multiple of divisor
                primefactors.append(divisor)
                currentint /= divisor
            else:
                divisor += 1
    if len(primefactors) == 0:
        print("{} is prime".format(givenint))
    else:
        #Find the duplicates and neatly put them to the power
        uniquefactors = []
        for factor in primefactors:
            if uniquefactors.count(factor) == 0:
                uniquefactors.append(factor)
        
        print("The factors of {} are:".format(givenint))
        
        for factor in uniquefactors:
            power =  primefactors.count(factor)
            if power == 1:
                print("\t{}".format(factor))
            else:
                print("\t{}^{}".format(factor, power))
    input("\n Press [Enter] to return to the main menu...")
    return

def binomial_natural():
    print("Binomial Expansion Coefficient table (natural numbers)\n\n")
    print("Form nCr, where r is a variable in a table, n is typically the power the binomial is raised to")
    
    #Variables for calculations in the format nCr
    n = intput("Give a value for n: ")
    r_start = intput("Value of r to start at (inclusive, 0 if you want all terms): ")
    r_end = intput("Value of r to end at (inclusive, equal to n if you want all terms): ")
    # r_stop is for the loop in Python
    r_stop = r_end + 1
    
    # For the table, the length of the r column will be the length of r_end + 1
    # At least 4
    r_col_length = len(str(r_end)) + 1
    if r_col_length < 4:
        r_col_length = 4
    print("For n = {}\n    r{} | nCr".format(n, " "*(r_col_length-4)))
    
    for x in range(r_start, r_stop):
        amount_of_spaces = r_col_length - len(str(x))
        print(" " + " "*amount_of_spaces + str(x) + " | {}".format(maths.comb(n, x)))

    input("\n Press [Enter] to return to the main menu...")
    return

def binomial_rational():
    print("Binomial Expansion Coefficient table (all rational numbers)\n\n")
    print("Form nCr, where r is a variable in a table, n is typically the power the binomial is raised to")
    
    #Variables for calculations in the format nCr
    n = floatput("Give a value for n: ")
    r_amount = intput("How many coefficients to find? (starting from x^0): ")
    
    # For the table, the length of the r column will be the length of r_amount + 1
    # At least 4
    r_col_length = len(str(r_amount)) + 1
    if r_col_length < 4:
        r_col_length = 4
    print("For n = {}\n    r{} | nCr".format(n, " "*(r_col_length-4)))
    
    for x in range(r_start, r_stop):
        amount_of_spaces = r_col_length - len(str(x))
        r_iteration = n
        for y in range(1, r_amount + 1):
            r_iteration *= (n - y)
        r_iteration /= maths.factorial(x)
        print(" " + " "*amount_of_spaces + str(x) + " | {}".format(r_iteration))

    input("\n Press [Enter] to return to the main menu...")
    return



#Menu
while not quitting:
    print("\n"*2)
    print("Select an option:\n")
    print("1) Quadratic equation solver")
    print("2) Quadratic inequality solver")
    print("3) Prime factor finder")
    print("4) Binomial Expansion Coefficient table (natural numbers)")
    print("5) Binomial Expansion Coefficient table (all rational numbers)")
    print("q) Quit")
    option = input("\n\nPick an option: ")
    if option == "1":
        quadratic()
    if option == "2":
        quadratic_inequality()
    if option == "3":
        primefactorise()
    if option == "4":
        binomial_natural()
    if option == "5":
        binomial_rational()
    if option == "q":
        quitting = True
        quit()
