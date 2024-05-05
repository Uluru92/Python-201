# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# If they choose the right door, then they encounter a dragon.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
player = str(input("CLI RPG GAME - Please enter your name: "))
print(player,"welcome to the game!")

door_selection = None
sword = False
continue_empty_room = None
continue_dragon_room = None
pickup_sword = None
fight_dragon = None

while door_selection != "left" and door_selection != "right": 
    door_selection = str(input("You have to select 1 door, make a choice: left or right?: "))

    if door_selection != "left" and door_selection != "right":
        print("Please try again, pick left o right, watch your grammar")
        
    elif door_selection == "left":
        print("---------------\n-              -\n-  EMPTY ROOM  -\n-              -\n---------------")
        door_selection = None #así volvemos a la elección entre left y right nuevamente

        while continue_empty_room != "yes" and continue_empty_room != "no":
            continue_empty_room = str(input("Do you want to go futher or return? (yes/no): "))

            if continue_empty_room == "yes":               

                while pickup_sword != "yes" and pickup_sword != "no" and sword == False:               
                    pickup_sword = str(input("You found a sword! Do you want to take it? (yes/no): ")) 

                    if pickup_sword == "yes":
                        print("Here it is! Pick it up!: -+----->")
                        sword = True #this way we confirm to pick up the sword!
                        
                    elif pickup_sword == "no":
                        print("Ok, you left the sword behind! Go back to the previus room")
                        sword = False #this way to make clear the player do not have the sword in his hands

                    else:
                        print("Please, enter yes if you want to keep it, or no if you want to leave it behind!")

                pickup_sword = None #reset the option to pick up the sword in case the player comes back later

                if sword == True:
                    print("Now the room is really empty, you already have the sword, go back to the previus room!")

            elif continue_empty_room == "no":
                print("Ok, return to the previous room!")

        continue_empty_room = None #reset the option to continue to the empty room in case the player comes back to this room later

    elif door_selection == "right":
        print("---------------\n-              -\n-  DRAGON****  -\n-              -\n---------------")

        while continue_dragon_room != "yes" and continue_dragon_room != "no":
            continue_dragon_room = str(input("Do you want to go futher or return?(yes/no): "))

            if continue_dragon_room == "yes":

                while fight_dragon != "yes" and fight_dragon != "no":
                    fight_dragon = str(input("Do you want to fight the dragon? (yes/no): "))

                    if fight_dragon == "yes" and sword == True:
                        print("Use your sword to kill the dragon! You won the game!")
                        exit(0)  # Successful exit

                    elif fight_dragon == "yes" and sword == False:
                        print("oh no! you don't have any weapons to kill the dragon! You lost the game!")
                        exit(0)  # Successful exit

                    elif fight_dragon == "yes" and sword == None:
                        print("oh no! you don't have any weapons to kill the dragon! You lost the game!")
                        exit(0)  # Successful exit
                    
                    elif fight_dragon == "no" and sword == True:
                        print("Ok, you could have killed the dragon, but ok, return to the previus room!")

                    elif fight_dragon == "no" and sword == False:
                        print("Ok, good choice because you are not prepared to kill the dragon yet! go find a weapon before coming back!")

                    elif fight_dragon == "no" and sword == None:
                        print("Ok, good choice because you are not prepared to kill the dragon yet! go find a weapon before coming back!")   
                    
                    else:
                        print("Please, enter 'yes' if you want to fight the dragon, or 'no' if you want to leave the room")
                        
                fight_dragon = None

            elif continue_dragon_room == "no":
                print("Ok, return to the previous room!")

        continue_dragon_room = None #reset the option to continue to the dragon room in case the player comes back to this room later

    door_selection = None

