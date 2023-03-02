import random 

player_score = 0
computer_score = 0

options = ["rock","paper","scissor"]

while True :
    player_input = input("Chose rock, paper, scissors or clik Q to quit: ").lower()
    if player_input == "q":
        break
    if player_input not in options:
        continue
    
    computer_bot = random.randint(0,2)
    computer_pick = options[computer_bot]
    print("Computer picked", computer_pick + ".")

    if player_input == computer_pick:
        print("Draw Game!")
    elif player_input == "rock" and computer_pick == "scissors":
        print("YOu win!")
        player_score += 1
    elif player_input == "paper" and computer_pick == "rock":
        print("YOu win!")
        player_score += 1
    elif player_input == "scissors" and computer_pick == "paper":
        print("You win")
        player_score += 1
    elif computer_pick== "paper" and player_input == "rock":
        print("YOu lose")
        computer_score += 1
    elif computer_pick == "scissors" and player_input == "paper":
        print("You lose")
        computer_score += 1
    elif computer_pick == "rock" and player_input == "scissors":
        print("You lose!")
        computer_score += 1
    

print("You won", player_score, " times.")
print("The computer won", computer_score, "times.")
print("Thank You to play game")



