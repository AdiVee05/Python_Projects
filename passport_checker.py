# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jack Gutacker
#               Cameron Jackson
#               Alan Ngo
#               Aditya Veeramony
# Section:      19
# Assignment:   lab 11
# Date:         29 10 2024
name = input("Enter the name of the file: ")
#"scanned_passports.txt"

file = open(name, "r")
names = (file.read()).split("\n\n")
validpassports = open("valid_passports.txt", "w")

v = 0
for i in range(len(names)):
    call = {}
    new = []
    current = names[i].split()
    for j in current:
        new.append(j.split(":"))
    valid = False
    for k in new:
        call[k[0]] = k[1]
        #this makes it into a dict
    if "byr" in call and "pid" in call and "cid" in call and "eyr" in call and "hcl" in call and "ecl" in call and "hgt" in call:
        valid = True
        #this checks to make sure its valid
    if valid == True:
        validpassports.write(names[i]+"\n\n")
        v += 1
validpassports.close()

print(f"There are {v} valid passports")