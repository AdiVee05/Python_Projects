print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
pathway = input("You're at a diverging path. Which direction do you go? Type 'left' or 'right'\n")
if pathway=="left":
    print("You chose the safe path. Now proceed onwards!!")
    river = input("You've reached a river. Will you swim or wait? \nType 'S' or 'W'\n")
    if river == "W":
        print("A boat rescued you! You crossed the river!")
        house = input("You reach a wooden cabin with three distinct doors. Red, Blue, and Yellow.\nWhich door will you choose? Type 'R', 'B', or 'Y'\n")
        if house == "R":
            print("You walk inside...INTO FUCKING FIRE! You're dead. Game Over.")
        elif house == "B":
            print("You walk inside...you turn the corner into a dinner room filled with delicous treats. You sit down. You're so happy that your're finally free\n....IS THAT A FUCKING BEAR! You try to run but the bear catches up with you. The bear along with it's buddies begin to tear you apart like the cotton candy you are. Note to self, don't choose the bear. Game Over.") 
        elif house == "Y":
            print("You walk inside...you enter a room filled to the brim with food, water, and all the supplies you need.\nYou jump up in joy, squealing like a little girl in 2008 who found out they got front row tickets to Justin Bieber's concert! Congrats YOU WON!. Now get out of my game. smh.")
        else:
            print("How the hell did you even mess up that bad. fml. GAME OVER.")
    else:
        print("While swimming you see a mysterious presence...A HUGE TROUT! You desperatley try to swim away from it but it's too late and you're eaten whole by the trout. Game Over.")

else:
    print("You've fallen into a big, deep hole that you can can never escape from. Game Over.")
    

        
