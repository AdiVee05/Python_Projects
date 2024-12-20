# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jack Gutacker
#               Cameron Jackson
#               Alan Ngo
#               Aditya Veeramony
# Section:      19
# Assignment:   lab 8
# Date:         17 10 2024

#jacks part

time = input("Enter the time: ")
timenew = time.split(":")
hours = timenew[0]
minuites = timenew[1]
timevalid = False
checker= "0123456789:"
validvar = True
while timevalid == False:
    timet = hours + minuites
    for i in timet:
        if i in checker:
            validvar = True
        else:
            validvar = False
            break
    var = validvar
    if var == True:
        if int(hours) <= 24 and int(minuites) < 60:
            timevalid = True
            break
        else:
            newt = input("Invalid time. Input new time: ")
            timenew = newt.split(":")
            hours = timenew[0]
            minuites = timenew[1]
    else:
        newt = input("Invalid time. Input new time: ")
        timenew = newt.split(":")
        hours = timenew[0]
        minuites = timenew[1]


clock_type = input("Choose the clock type (12 or 24): ")
#camerons part
hr = int(hours)
mn = minuites
#splices to get hrs and minutes without ':'
am = 0
valid = True
if clock_type == '12':
    if hr < 12:
        am = 0
    elif hr >= 12:
        am = 1
    if hr > 12:
        hr -= 12
elif clock_type == '24':
    time = time
    am = 2
else:
    valid = False
#Checks clock type and adds am pm
while valid == False:
    clock_type = input('Invalid! Choose the clock type (12 or 24):')
    if clock_type == '12':
        if hr < 12:
            am = 0
        elif hr >= 12:
            am = 1
        if hr > 12:
            hr -= 12
        valid = True
    elif clock_type == '24':
        time = time
        am = 2
        valid = True
#checks for valid time and request input if not valid
#jack part continued
if hr == 0:
    hr = 12
chara = input("Enter your preferred character: ")
first =  ["111"," 1 ","111","111", "1 1","111", "111", "111", "111", "111", " ", " A ", "PPP", "M   M"]
second = ["1 1","11 ","  1","  1", "1 1","1  ", "1  ", "  1", "1 1", "1 1", ":", "A A", "P P","MM MM"]
third =  ["1 1"," 1 ","111","111", "111","111", "111", "  1", "111", "111", " ", "AAA","PPP","M M M"]
fourth = ["1 1"," 1 ","1  ","  1", "  1","  1", "1 1", "  1", "1 1", "  1", ":", "A A","P  ","M   M"]
fifth =  ["111","111","111","111", "  1","111", "111", "  1", "111", "111", " ", "A A","P  ","M   M" ]
varsforlist = [first, second, third, fourth, fifth]
new1 = []
new2 = []
new3 = []
new4 = []
new5 = []
newtime = [new1, new2, new3, new4, new5]
chars = "abcdeghkmnopqrsuvwxyz@$&*= "
valid = False
if chara in chars:
    valid = True
while valid == False:
    new = input("Character not permitted! Try again: ")
    if new in chars:
        valid = True
        chara = new
        break
print()
#alan part
# Time representation as digits
digits = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, ':': 10
}

# creates time in specific format
def display_time(hours, minuites):
    time_str = (str(hours) + str(minuites))
    rows = [[],[],[],[],[]]
    for digit in time_str:
        index = digits[digit]
        rows[0] = rows[0] + [first[index]]
        rows[1] = rows[1] + [second[index]]
        rows[2] = rows[2] + [third[index]] 
        rows[3] = rows[3] + [fourth[index]]
        rows[4] = rows[4] + [fifth[index]] 
    return(rows)

#aadi part
new_list = display_time(hr, mn)
count = str(hr) + str(mn)
if chara == "":
   for i in new_list:
        step = 0
        for w in i:
            new = str(w)
            var = new.replace("1",count[step]) 
            i[step] = var
            step += 1

else:
    for i in new_list:
        step = 0
        for w in i:
            new = str(w)
            var = new.replace("1",chara) 
            i[step] = var
            step += 1
if len(count) == 3:
    for i in range(0, 5):
        new_list[i].insert(1, varsforlist[i][10])
else:
    for i in range(0, 5):
        new_list[i].insert(2, varsforlist[i][10])
#this checks and insertes the colon
if am == 0:
    for i in range(0, 5):
        new_list[i].append(varsforlist[i][11])
        new_list[i].append(varsforlist[i][13])

elif am == 1:
    for i in range(0, 5):
        new_list[i].append(varsforlist[i][12])
        new_list[i].append(varsforlist[i][13])

for i in new_list:
    print(*i, sep=" ")