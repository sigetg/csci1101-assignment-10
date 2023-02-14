# Write a program that works with fractions.  Your program will read two
# fractions of the form a/b and an operation (+, -, *, /) from the user, then
# perform the requested operation and print the results.
#
# You are required to create 10 functions to solve this problem.  This may seem
# like a lot, but each one taken on its own is simple.  Most of the functions
# will take fractions as parameters, return fractions, or both.  You are
# required to represent each fraction as a dictionary.  Specifically, each
# fraction will be a dictionary with two key-value pairs.  The key "numerator"
# will be mapped to the numerator for the fraction, and the key "denominator"
# will be mapped to the denominator for the fraction.  For example, if we have
# the fraction 3/4 then the dictionary for that fraction will be
# {"numerator": 3, "denominator": 4}.  All function parameters and return values
# that are fractions must be handled with dictionaries of this form.
#
# Here are the details of the functions:
#
# gcd(): two integer parameters; returns the greatest common divisor of the two
#     parameters.
#     + We did this in the week 7 discussion section.
#     + You need it for the next function.
# simplify_fraction(): one fraction (dictionary) parameter; returns a new
#     fraction that is the simplified version of the parameter fraction.
#     + You'll need to use your gcd() function here.
#     + Be sure to return a new fraction (dictionary) rather than modifying the
#       provided one.
# get_fraction(): no parameters; returns a new fraction (dictionary) that is
#     read from the user.
#     + The user will enter a fraction as a/b (no spaces around the /).  You
#       will have to read in the input as a string then use string.split() with
#       a parameter to get the two numbers.
#     + If the input is not in the right format, then print an error message and
#       exit.  This includes if the user provides numerator or denominator
#       values that aren't integers.  You'll need to use try/except for this
#       part.
#     + If the provided denominator is zero, that is also an error.  Print an
#       error and exit.
#     + The fraction should be returned in simplified form.
# get_operation(): no parameters; returns the operation string (+, -, *, or /).
#     + If the user enters anything that is not one of the 4 valid operations,
#       print an error and exit.
# add_fractions(): two fraction (dictionary) parameters; returns a new fraction
#     that is the sum of the two parameters.
#     + Return the new fraction in simplified form.
# subtract_fractions(): two fraction (dictionary) parameters; returns a new
#     fraction that is the difference of the two parameters.
#     + Return the new fraction in simplified form.
# multiply_fractions(): two fraction (dictionary) parameters; returns a new
#     fraction that is the two parameter fraction multiplied together.
#     + Return the new fraction in simplified form.
# divide_fractions(): two fraction (dictionary) parameters; returns a new
#     fraction that is the first parameter fraction divided by the second
#     parameter fraction.
#     + Return the new fraction in simplified form.
#     + If the second parameter fraction's numerator is zero, then print an
#       error and exit (can't divide by zero!).
# print_fraction(): one fraction (dictionary) parameter; no return value.
#     + Prints the fraction in the standard a/b form.
#     + If the fraction's denominator is 1, then print it without the "/1".
#     + The function should not print the fraction on it's own line, to help
#       with the next function.
# print_results(): four parameters: the first fraction (dictionary) from the
#     user, the operation from the user, the second fraction (dictionary) from
#     the user, and the result fraction (dictionary) from the operation; no
#     return value.
#     + The function will use print_fraction() to print each fraction in the
#       right format.
#     + The output should all be on one line.
#
# The main program will call get_fraction() twice, get_operation(), the
# appropriate math function based on the operation, and print_results().  The
# main code should be simple and easy to read if you've done everything
# correctly.  Note that the instructor's solution (without comments) is just shy
# of 100 lines of Python.  If you are working towards a solution that is much
# longer (or shorter) than that, then you're probably headed in the wrong
# direction.
#
# More importantly, be sure to take this problem one step at a time.  Test your
# code early and often.  For example, start by writing get_fraction(), then
# printing the fraction in your main code, just to test.  Slowly add each
# requirement to get_fraction() until you know it's working correctly.  Then add
# get_operation(), then an easier math function like multiply_fractions().
# Once that's working, you can write and test print_fraction(), then
# print_results().  Then go back to finish the other three math functions.
# Finally, add in the gcd() and simplify_fraction() functions and use them in
# get_fraction() and the math functions to return fractions in simplified form.
# Once again, don't write dozens of lines of code or several functions without
# testing your code as you go!
#
# Your input and output messages must conform to the following examples:
#
# Enter a fraction (a/b): 1.2
# Error! Fractions are of the form a/b, where and b are integers.
#
# Enter a fraction (a/b): 1/2/3
# Error! Fractions are of the form a/b, where and b are integers.
#
# Enter a fraction (a/b): a/2
# Error! Fractions are of the form a/b, where and b are integers.
#
# Enter a fraction (a/b): 1/0
# Error! Can't have a zero denominator.
#
# Enter a fraction (a/b): 1/2
# Enter operation (+,-,*,/): add
# Error! Operation must be +,-,*,/.
#
# Enter a fraction (a/b): 1/2
# Enter operation (+,-,*,/): +
# Enter a fraction (a/b): 1/3
# 1/2 + 1/3 = 5/6
#
# Enter a fraction (a/b): 1/-2
# Enter operation (+,-,*,/): +
# Enter a fraction (a/b): -4/3
# -1/2 + -4/3 = -11/6
#
# Enter a fraction (a/b): 1/2
# Enter operation (+,-,*,/): -
# Enter a fraction (a/b): -1/2
# 1/2 - -1/2 = 1
#
# Enter a fraction (a/b): 1/4
# Enter operation (+,-,*,/): *
# Enter a fraction (a/b): 0/10
# 1/4 * 0 = 0
#
# Enter a fraction (a/b): 1/2
# Enter operation (+,-,*,/): /
# Enter a fraction (a/b): 0/10
# Error! Can't divide by a zero fraction.
#
# Enter a fraction (a/b): 2/4
# Enter operation (+,-,*,/): /
# Enter a fraction (a/b): 15/10
# 1/2 / 3/2 = 1/3
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import sys

def gcd(int_1, int_2):
    while int_2 != 0:
        x = int_2
        int_2 = int_1 % int_2
        int_1 = x
    return int_1

def simplify_fraction(frac_dict):
    simple_frac_dict = {}
    a = frac_dict["numerator"]
    b = frac_dict["denominator"]
    c = gcd(a, b)
    simple_frac_dict["numerator"] = int(a / c)
    simple_frac_dict["denominator"] = int(b / c)
    return simple_frac_dict

def get_fraction():
    frac_dict = {}
    str_frac = input("Enter a fraction (a/b): ")
    try:
        frac_list = str_frac.split("/")
        if len(frac_list) > 2:
            sys.exit()
        frac_dict["numerator"] = int(frac_list[0])
        frac_dict["denominator"] = int(frac_list[1])
        
    except:
        print("Error! Fractions are of the form a/b, where a and b are integers.")
        sys.exit()
    if frac_dict["denominator"] == 0:
        print("Error! Can't have a zero denominator.")
        sys.exit()
    return frac_dict

def get_operation():
    op = input("Enter operation (+,-,*,/): ")
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Error! Operation must be +,-,*,/.")
        sys.exit()
    return op

def add_fractions(frac_dict_1, frac_dict_2):
    numerator_sum = frac_dict_1["numerator"] * frac_dict_2["denominator"] + frac_dict_2["numerator"] * frac_dict_1["denominator"]
    denominator_sum = frac_dict_1["denominator"] * frac_dict_2["denominator"]
    sum_frac_dict = {}
    sum_frac_dict["numerator"] = numerator_sum
    sum_frac_dict["denominator"] = denominator_sum
    final_frac = simplify_fraction(sum_frac_dict)
    return final_frac

def subtract_fractions(frac_dict_1, frac_dict_2):
    numerator_dif = frac_dict_1["numerator"] * frac_dict_2["denominator"] - frac_dict_2["numerator"] * frac_dict_1["denominator"]
    denominator_dif = frac_dict_1["denominator"] * frac_dict_2["denominator"]
    dif_frac_dict = {}
    dif_frac_dict["numerator"] = numerator_dif
    dif_frac_dict["denominator"] = denominator_dif
    final_frac = simplify_fraction(dif_frac_dict)
    return final_frac

def multiply_fractions(frac_dict_1, frac_dict_2):
    numerator_prod = frac_dict_1["numerator"] * frac_dict_2["numerator"]
    denominator_prod = frac_dict_1["denominator"] * frac_dict_2["denominator"]
    prod_frac_dict = {}
    prod_frac_dict["numerator"] = numerator_prod
    prod_frac_dict["denominator"] = denominator_prod
    final_frac = simplify_fraction(prod_frac_dict)
    return final_frac

def divide_fractions(frac_dict_1, frac_dict_2):
    if frac_dict_2["numerator"] == 0:
        print("Error! Can't have a zero denominator.")
        sys.exit()
    numerator_prod = frac_dict_1["numerator"] * frac_dict_2["denominator"]
    denominator_prod = frac_dict_1["denominator"] * frac_dict_2["numerator"]
    prod_frac_dict = {}
    prod_frac_dict["numerator"] = numerator_prod
    prod_frac_dict["denominator"] = denominator_prod
    final_frac = simplify_fraction(prod_frac_dict)
    return final_frac

def print_fraction(frac_dict):
    if frac_dict["denominator"] == 1:
        print(frac_dict["numerator"], end="")
    elif frac_dict["numerator"] == 0:
        print(frac_dict["numerator"], end="")
    else:
        print(frac_dict["numerator"],"/",frac_dict["denominator"], sep="", end="")

def print_results(frac_dict_1, op, frac_dict_2, final_frac):
    print_fraction(frac_dict_1)
    print("", op, "", end="")
    print_fraction(frac_dict_2)
    print(" = ", end="")
    print_fraction(final_frac)

frac_dict_1 = get_fraction()
op = get_operation()
frac_dict_2 = get_fraction()

if op == "+":
    final_frac = add_fractions(frac_dict_1, frac_dict_2)
elif op == "-":
    final_frac = subtract_fractions(frac_dict_1, frac_dict_2)
elif op == "*":
    final_frac = multiply_fractions(frac_dict_1, frac_dict_2)
elif op == "/":
    final_frac = divide_fractions(frac_dict_1, frac_dict_2)

print_results(frac_dict_1, op, frac_dict_2, final_frac)













