#A rock, paper, scissors game
#importing random
from random import randint
our_list = ["Rock", "Paper", "Scissors"]

opponent = our_list[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?: ")
    if player == opponent:
        print("It is a tie.")
    elif player == "Rock":
        if opponent == "Paper":
            print("What a bummer, you lost.", opponent, "wraps", player, "like a burrito!")
        else:
            print("Congrats, you've won!!", player, "annihilate", opponent)
    elif player == "Paper":
        if opponent == "Scissors":
            print("What a bummer, you lost!", opponent, "cuts", player)
        else:
            print("Congrats, you've won", player, "wraps", opponent, "like a burrito")
    elif player == "Scissors":
        if opponent == "Rock":
            print("What a bummer, you lost!", opponent, "anihilates", player, "like a burrito")
        else:
            print("Congrats, you've won!", player, "cuts", opponent)

    else:
        print("What fo you mean? I dont understand!")

    player = False
    opponent = our_list[randint(0,2)]
    
        





































