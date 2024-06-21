import os
from random import randint as com

# Clears the console screen
os.system('cls')

# Takes input from the user for their selection
p1 = int(input("1 - for Fold  \n2 - for Unfold \nSelect your number: ")) - 1

# Generates random selections for computer players
c1, c2 = com(0, 1), com(0, 1)

# Checks if the user input is valid (0 for Fold, 1 for Unfold)
if p1 not in [0, 1]:
    print("Invalid Selection")
else:
    # Maps the selection to their corresponding actions
    selection = ["Fold", "Unfold"]
    player, com1, com2 = selection[p1], selection[c1], selection[c2]
    
    # Prints the selections of the player and computers
    print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")
    
    # Determines the winner based on the selections
    if p1 != c1 and p1 != c2:
        result = "Player 1 wins"
    elif c1 != p1 and c1 != c2:
        result = "Computer 1 wins"
    elif c2 != p1 and c2 != c1:
        result = "Computer 2 wins"
    else:
        result = "DRAW!!!"

    # Prints the result
    print(result)

