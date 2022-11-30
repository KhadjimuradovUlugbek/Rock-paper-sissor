import random
choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

player = False

cpu_score = 0
player_score = 0

print("To finish the game please write 'end'")

while True:
    player = input("Rock,Paper or Scissors?").capitalize()
    #Conditions of Rock,Paper amd Scissors
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
           print("You lose!", computer, "covers", player)
           cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win", player, "covers", computer)
            player_score+=1
    elif player=='End':
        print("Final scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break