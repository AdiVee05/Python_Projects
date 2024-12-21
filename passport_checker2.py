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
validpassports = open("valid_passports2.txt", "w")

def validpass(byr, eyr, hgt, hcl, ecl, pid, cid):
    val = True
    eyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if int(byr) < 1920 or int(byr) > 2008:
        val = False   
    if int(eyr) < 2024 or int(eyr) > 2034:
        val = False
    if hgt[-2:] == "cm" or hgt[-2:] == "in":
        if hgt[-2:] == "cm":
            if int(hgt[:-2]) < 150 or int(hgt[:-2])> 193:
                val = False
        elif hgt[-2:] == "in":
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) >76:
                val = False
    else:
        val = False

    hc = hcl[1:]
    correct = "0123456789abcdef"
    if len(hc) == 6:
        for i in hc:
            if i not in correct:
                val = False
    else:
        val = False

    if ecl not in eyecolor:
        val = False


    if len(pid) != 9:
        val = False


    if len(str(int(cid))) != 3:
        val = False
    return(val)




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
        validagain = validpass(call["byr"], call["eyr"], call["hgt"], call["hcl"], call["ecl"], call["pid"], call["cid"])
        if validagain == True:
            validpassports.write(names[i]+"\n\n")
            v += 1
validpassports.close()

print(f"There are {v} valid passports")