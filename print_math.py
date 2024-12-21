# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aditya Veeramony
# Section:      467/567, 568, 474/574
# Assignment:   Lab 1
# Date:         21st of August, 2024

import math 

# Reynolds Number

# variable for fluid velocity 
fv = 9
# variable for kinematic viscosity 
kv = .0015
# variable for linear dimension 
ld = .875

# Reynolds number as equation
reynolds_number = ((fv*ld)/kv)

print("Reynolds number is" , reynolds_number)

# Wavelength of x-rays

# variable for crystal lattice distance
cld = .028
# scattering angle conversion to radians from degrees
scattering_angle = math.radians(35)
# scattered angle used with sin function
final_sa = math.sin(scattering_angle)

# Wavelength
wl = (2*.028)*final_sa

print("Wavelength is", wl, "nm")

# Arps Equation

#time
t = 10
# intial production rate
qi = 100
# intial decline rate
Di = 2 
# hyperbolic constant 
b = .8

#Equation
arps = (qi/(math.pow((1+(b*Di*t)),(1/b))))
print("Production rate is", arps , "barrels/day")

# Tsiolkovsky Rocket Equation

# intial mass
im = 11000
# final mass
fm = 8300
# exhaust velocity
ev = 2028

#Equation
tre = (2028*(math.log(im/fm)))
print("Change of velocity is", tre , "m/s")