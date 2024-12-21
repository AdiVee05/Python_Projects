# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jack Gutacker
#               Cameron Jackson
#               Alan Ngo
#               Aditya Veeramony
# Section:      19
# Assignment:   lab 4.16
# Date:         5 9 2024
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))
# Variables
x1 = "x^2"
first = "+"
second = " + "
third = " + "
x = "x"
# If Sequence
if a >0:
    first = ""
elif a < 0:
    first = "- "
    a = a *-1
if a == 1 or a == -1:
    a = ""
if a == 0:
    first = ""
    a = ""
    x1 = ""
    second = ""
if b < 0:
    b = b * -1
    second = " - "
if b ==1 or b == -1:
    b = ""
if b == 0:
    second = ""
    b = ""
    x = ""
if c < 0:
    c = c * -1
    third = " - "
if c == 0:
    third = ""
    c = ""
print(f"The quadratic equation is {first}{a}{x1}{second}{b}{x}{third}{c} = 0")
