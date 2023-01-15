import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock")
print(rock)
print("Paper")
print(paper)
print("Scissors")
print(scissors)
choices=[rock,paper,scissors]
choice=["Rock","Paper","Scissors"]
a= random.randint(0,2)

b= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("\n")
if (b>=3):
    print("Please enter a valid choice.")
else:
    if (a==b):
       print("Tie")
    elif (a==0 and b==1):
       print("Yoooo You Won.")
    elif (a==0 and b==2):
       print("Noooo You Lose.")
    elif (a==1 and b==0):
       print("Noooo You Lose.")    
    elif (a==1 and b==2):
       print("Yoooo You Won.")
    elif (a==2 and b==0):
       print("Yoooo You Won.")
    elif (a==2 and b==1):
       print("Noooo You Lose.")

    c= choices[a]
    e= choice[a]
    d= choices[b]
    f= choice[b]
    print("\n")
    print(f"You have chosen {f} :")
    print(f"{d}")
    print(f"The computer has chosen {e}:")
    print(f"{c}")
