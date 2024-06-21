import os
from random import randint as com

os.system('cls')

p1 = int(input("1 - for Fold  \n2 - for Unfold \nSelect your number: ")) - 1
c1, c2 = com(0, 1), com(0, 1)

if p1 not in [0, 1]:
    print("Invalid Selection")
else:
    selection = ["Fold", "Unfold"]
    player, com1, com2 = selection[p1], selection[c1], selection[c2]
    print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")
    
    if p1 != c1 and p1 != c2:
        result = "Player 1 wins"
    elif c1 != p1 and c1 != c2:
        result = "Computer 1 wins"
    elif c2 != p1 and c2 != c1:
        result = "Computer 2 wins"
    else:
        result = "DRAW!!!"

    print(result)
