import random

def DiceRoll():
    print(random.choice(range(6)))
    
choice = input(f"Would you like to roll the dice? \nYes(1) or No(2): ")

def play():
    
    global choice
    
    if choice == 1:
        DiceRoll()
    elif choice == 2:
        exit
    else:
        print("Please select a choice")

play()