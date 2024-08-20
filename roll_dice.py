import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    
    roll = input("\nRoll the dice? (Yes/No) : \n")
    while roll.lower() == "Yes".lower():
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            print(f"\ndice rolled: {dice1} and {dice2}\n")
            print("\n".join(dice_drawing[dice1]))
            print("\n".join(dice_drawing[dice2]))
        
            roll = input("\nRoll again? (Yes/no): \n")
            print("\nGame Ended 👋\n") 
           
      

roll_dice()