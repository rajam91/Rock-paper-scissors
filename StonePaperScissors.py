import random

while True:
    player = input("Enter [rock, paper, scissors]: ")
    choose =   ["rock", "paper", "scissors"]
    computer = random.choice(choose)

    print(f"You choose {player}, computer choose {computer}")

    if player == computer:
        print("Tie...")

    elif player == "rock":
        if computer == "scissors":
            print("You win !")
        else:
            print("You loose :( ")

    elif  player == "paper":
        if computer == "rock":
            print("You win !")
        else:
            print("You loose :( ")
    
    elif player == "scissors":
        if computer == "paper":
            print("You win !")
        else:
            print("You loose :( ")
    continue
