import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice([1, 2, 3])
    player = None
    while player not in [1, 2, 3]:
        player = int(input("1-rock \n2-paper \n3-scissors \nchoose: "))
    if player == computer:
        print("Tie!")
    elif player == 1:
        if computer == 2:
            print("Sorry, computer wins")
        else:
            print("You Win!")
    elif player == 2:
        if computer == 3:
            print("Sorry, computer wins")
        else:
            print("You Win!")
    elif player == 3:
        if computer == 1:
            print("Sorry, computer wins")
        else:
            print("You Win!")
    print("player: ", choices[player - 1])
    print("computer: ", choices[computer - 1])
    cont = input("continue (yes/no)? :").lower()
    if cont == "no":
        break
print("Finished, see you later!")
