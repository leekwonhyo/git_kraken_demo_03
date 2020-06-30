from random import randint

# list of play options
play = ["Rock", "Paper", "Scissors"]

<<<<<<< master
# list of messages
messages = ["Tie!", "You win!", "You lose!"]

# game rule
winning_rule = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

# get the user input
player = input("Rock", "Paper", "Scissors? ")

# assign a random play to the computer
computer = play[randint(0, 2)]
print('Computer: {}'.format(computer))

# ite
if player == computer:
    print(message[0])

# you win
elif winning_rule[player] == computer:
    print(messages[1])

# you lose
else:
    print(messages[2])
=======
while True:
    # get the user input
    player = input("Rock", "Paper", "Scissors? ")

    # assign a random play to the computer
    computer = play[randint(0, 2)]
    print('Computer: {}'.format(computer))

    # tie
    if player == computer:
        print("Tie!")
    
    # rock
    elif player == "Rock":
        if computer == "Scissors":
            print("You win!")
        else:
            print("you lose!")
    
    # paper
    elif player == "Paper":
        if computer == "Rock":
            print("You win!")
        else:
            print("you lose!")

    # scissors
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!")
        else:
            print("you lose!")

    # quit
    else:
        break
    
    # new line
    print()

# bye
print("Bye!")
>>>>>>> Introduce an infinite loop
