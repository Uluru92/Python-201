#Rock-Paper-Scissors Game
#Code a game of rock paper scissors.
#Instructions
#take in a number 0-2 from the user that represents their hand
#generate a random number 0-2 to use for the computer's hand
#call the function get_hand to get the string representation of the user's hand
#call the function get_hand to get the string representation of the computer's hand
#call the function determine_winner to figure out who won
#print out the player hand and computer hand
#print out the winner
#Some Tips
#Creating a function that gets a "hand" based on a number.
#The function should take in a number and return the string representation of the hand. E.g.:
#def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    # pass
#Pseudocodigo... let's go!

from random import randint

def get_hand(choice: int)-> str:
    sentence = ""
    rps = ""
    if choice == 0:
        rps += "rock"
        sentence += f"Choice made: {rps}"
    elif choice == 1:
        rps += "paper"
        sentence += f"Choice made: {rps}"
    elif choice == 2:
        rps += "scisors"
        sentence += f"Choice made: {rps}"
    else:
        sentence += "Please select 0 for rock, 1 for paper and 2 for scisors"

    return(rps)

#Player choice...
choice = int(999) #This way we get sure the player only picks 0, 1 or 2...
while choice !=0 and choice != 1 and choice !=2:
    choice = int(input("Please select 0 for rock, 1 for paper and 2 for scisors: "))
player_choice = get_hand(choice)
print("Choice by player: ", player_choice)

#Computer choice...
computer_choice = randint(0,2)
computer_choice_rps = get_hand(computer_choice)
print("Computer choice: ", computer_choice_rps)

#Lets play...
if player_choice == "rock" and computer_choice_rps == "rock":
    print("Its a draw!")
elif player_choice == "rock" and computer_choice_rps == "paper":
    print("You lose!")
elif player_choice == "rock" and computer_choice_rps == "scisors":
    print("You won!")
elif player_choice == "paper" and computer_choice_rps == "paper":
    print("Its a draw!")
elif player_choice == "paper" and computer_choice_rps == "scisors":
    print("You lose!")
elif player_choice == "paper" and computer_choice_rps == "rock":
    print("You won!")
elif player_choice == "scisors" and computer_choice_rps == "scisors":
    print("Its a draw!")
elif player_choice == "scisors" and computer_choice_rps == "rock":
    print("You lose!")
elif player_choice == "scisors" and computer_choice_rps == "paper":
    print("You won!")


