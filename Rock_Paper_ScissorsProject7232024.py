import random

your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
computer_choice = random.randint(0,2)
print(computer_choice)
if your_choice == "0":
    print("Your choice is Rock.")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif your_choice == "1":
    print("Your choice is Paper.")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("Your choice is Scissors.")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print("Computer chose:")


if computer_choice == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if your_choice=="0" and computer_choice==0:
    print("It is a draw.")
if your_choice=="0" and computer_choice==1:
    print("You lose.")
if your_choice=="0" and computer_choice==2:
    print("You win.")

if your_choice=="1" and computer_choice==0:
    print("You win.")
if your_choice=="1" and computer_choice==1:
    print("It is a draw.")
if your_choice=="1" and computer_choice==2:
    print("You lose.")

if your_choice=="2" and computer_choice==0:
    print("You lose.")
if your_choice=="2" and computer_choice==1:
    print("You win.")
if your_choice=="2" and computer_choice==2:
    print("It is a draw.")



















