# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aditya Veeramony
# Section:      467/567, 568, 474/574
# Assignment:   Lab 4
# Date:         17st of September, 2024

import math

nom = float(input("Enter the nominal diameter: "))
act = float(input("Enter the actual diameter: "))

sub = nom - act
avg = (nom+act)/2
sub_abs = math.fabs(sub)
value = (sub_abs/avg)*100

# Checks the statements for whether they are true or not
if value < 1:
    print("The diameter is within " + '<1%' + ' of desired value')
elif 1<=value<=2:
    print(f'The diameter is between 1% and <2% of desired value')
elif 2<=value<=5:
    print(f'The diameter is between 2% and <5% of desired value')
elif value > 5:
    print(f'Out of specifications, >=5% error')