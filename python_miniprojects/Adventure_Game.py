#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

player = str(input("CLI RPG GAME - Please enter your name: "))
life_points = 3
print("       __  ")
print("      ^  ^")
print("    ( 0  0  )")
print("     ( °   )","    ",player,"welcome to the game! You have", life_points,"Life points, good luck!")
print("      |___|")
print("       | |")
print("    .-#---#-.")
print("   || # | # ||")
print("  ||  | # |  ||")
print(" ||   |___|   ||")
print(" ||   |   |   ||")
print(" ||   |   |   ||")
print(" ||   |___|  ||")
print("  ||  | # | ||")
print("   || | # |||")
print("    .-#---#-.")
print("       |||")
print("        !!")
print("  -------  -------  -------  -------  -------")
print("  | ROOM 1  |  | ROOM 2  |  | ROOM 3  |  | ROOM 4  |  | ROOM 5  |")
print("  -------  -------  -------  -------  -------")



door_selection = None
sword = False
shield = False
continue_empty_room = None
continue_dragon_room = None
pickup_sword = None
fight_dragon = None

inventory = set()

while door_selection != 1 and door_selection != 2 and door_selection != 3 and door_selection != 4 and door_selection != 5: 
    door_selection = int(input("You have to select a door, make a choice: 1|2|3|4|5: "))

    if door_selection != 1 and door_selection != 2 and door_selection != 3 and door_selection != 4 and door_selection != 5:
        print("Please try again kid, you can only pick a room from the following numbers: 1|2|3|4|5")

    elif door_selection == 1:
        print("---------------------------------")
        print("-                               -")
        print("-                               -")
        print("-                               -")
        print("-  Seems like an empty room..!  -")
        print("-                               -")
        print("-                         *     -")
        print("-                               -")
        print("---------------------------------")

        door_selection = None #así volvemos a la elección entre left y right nuevamente

        while continue_empty_room != "yes" and continue_empty_room != "no":
            continue_empty_room = str(input("Do you want to go futher or return? (yes/no): "))
            continue_empty_room.lower()

            if continue_empty_room == "yes":               

                while pickup_sword != "yes" and pickup_sword != "no" and sword == False:               
                    pickup_sword = str(input("You found a sword! Do you want to add it to your inventory? (yes/no): ")) 

                    if pickup_sword == "yes":
                        print("     Here it is! Pick it up!         ")
                        print("#####################################")
                        print("##                                 ##")
                        print("##                                 ##")
                        print("##        ||IRON AGE SWORD||       ##")
                        print("##                                 ##")
                        print("##         =|========}>>           ##")
                        print("##                                 ##")
                        print("##                                 ##")
                        print("#####################################")
                        print("                                     ")
                        inventory.add("sword")
                        print("*Now this is your inventory:", inventory)
                        sword = True #this way we confirm to pick up the sword!

                    elif pickup_sword == "no":
                        print("Ok, you left the sword behind! Go back to the previus room")
                        sword = False #this way to make clear the player do not have the sword in his hands

                    else:
                        print("Please, enter yes if you want to keep it, or no if you want to leave it behind!")

                pickup_sword = None #reset the option to pick up the sword in case the player comes back later

                while go_futher_empty_room != "yes" and go_futher_empty_room != "no":
                    go_futher_empty_room = str(input("Do you want to go even futher or return to the main room? (yes/no): "))
                    go_futher_empty_room.lower()

                    if go_futher_empty_room == "yes":
                        pickup_shield = str(input("You found a shield! Do you want to add it to your inventory? (yes/no): ")) 

                        if pickup_shield == "yes":
                            print("  Here it is! Pick it up!  ")
                            print("###########################")
                            print("##                       ##")
                            print("##  ||PALADIN SHIELD||   ##")
                            print("##                       ##")
                            print("##          ,-.          ##")
                            print("##         /   \         ##")
                            print("##        /     \        ##")
                            print("##       /       \       ##")
                            print("##      |         \      ##")
                            print("##      |    _     |     ##")
                            print("##      |    _     |     ##")
                            print("##      |    _     |     ##")
                            print("##      |          |     ##")
                            print("##      |         /      ##")
                            print("##       \       /       ##")
                            print("##        \     /        ##")
                            print("##         \   /         ##")
                            print("##          \-/          ##")
                            print("##                       ##")
                            print("##                       ##")
                            print("###########################")
                            print("                           ")

                        inventory.add("shield")
                        print("*Now this is your inventory:", inventory)
                        shield = True #this way we confirm to pick up the sword!

            elif continue_empty_room == "no":
                print("Ok, return to the previous room!")

        continue_empty_room = None #reset the option to continue to the empty room in case the player comes back to this room later

    elif door_selection == 2:
        print("                  ,-.        ,-.                    ")
        print("                 /   \      /   \                   ")
        print("                /     \    /     \                  ")
        print("              /   .--.  /   .--.  \                 ")
        print("             |  /  oo \ | /  oo \  |                ")
        print("             | |  ^   | |  ^   | |                  ")
        print("             | '--'   '--'   '--' |                 ")
        print("             |       |       |       |              ")
        print("             |       |       |       |              ")
        print("       .--.   |       |       |    .--.             ")
        print("      /    \  |   .--.  .--.  |   /    \            ")
        print("    /  .--. \ |  /    \  /    \  | /  .--. \        ")
        print("    | |    | || |      | |      || |    | |         ")
        print("    | |    | || |      | |      || |    | |         ")
        print("     \ '--' /  | |   .--.  .--.   |  \ '--' /       ")
        print("      \___/    | |  /    \  /    \  |   \___/       ")
        print("       '-'        '-'        '-'                    ")

        while continue_dragon_room != "yes" and continue_dragon_room != "no":
            continue_dragon_room = str(input("Do you want to go futher or return?(yes/no): "))

            if continue_dragon_room == "yes":

                while fight_dragon != "yes" and fight_dragon != "no":
                    fight_dragon = str(input("Do you want to fight the dragon? (yes/no): "))
                    fight_dragon.lower()

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
    elif door_selection == 3:
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
   
    elif door_selection == 4:
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
    elif door_selection == 5:
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
    elif door_selection == "Roll the dice":
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