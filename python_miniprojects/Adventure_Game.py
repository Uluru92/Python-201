#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

player = str(input("CLI RPG GAME - Please enter your name: "))
life_points = 1
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

room_1 = None #WHERE YOU CAN FIND A SWORD AND A SHIELD...
go_futher_room_1 = None
pickup_sword = None
pickup_shield = None

room_2 = None
continue_dragon_room = None
fight_dragon = None

room_2 = None
get_bless = None

inventory = set()

while door_selection == None:
    door_selection = input("You have to select a door, make a choice: 1|2|3|4|5: ")
    if door_selection not in "12345":
        print("Please try again kid, you can only pick a room from the following numbers: 1|2|3|4|5")
    else:
        door_selection = int(door_selection)         
        if door_selection == 1 and "sword" not in inventory or "shield" not in inventory:
            print("---------------------------------")
            print("-                               -")
            print("-                               -")
            print("-                               -")
            print("-  Seems like an empty room..!  -")
            print("-                          .    -")
            print("-  WAIT! what is that?!   .*.   -")
            print("-                               -")
            print("---------------------------------")
            while room_1 != "yes" and room_1 != "no":
                room_1 = str(input("Do you want to take a look around? (yes/no): "))
                room_1 = room_1.lower()            
                if room_1 == "yes": 
                    if "sword" not in inventory:
                        while pickup_sword != "yes" and pickup_sword != "no":               
                            pickup_sword = str(input("You found a sword! Do you want to add it to your inventory? (yes/no):")) 
                            pickup_sword = pickup_sword.lower()
                            if pickup_sword == "yes":
                                inventory.add("sword")
                                print("                                     ")
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
                                print("*Now this is your inventory:", inventory)
                            elif pickup_sword == "no":
                                print("Not the best choice kid...")
                            else:
                                print("Please, enter YES if you want to keep it, or NO if you want to leave it behind!")
                        pickup_sword = None
                    elif "sword" in inventory:
                        print("Seems like there is nothing else here...")
                    while go_futher_room_1 != "yes" and go_futher_room_1 != "no":
                        go_futher_room_1 = str(input("Do you want to go even futher? (yes/no): "))
                        go_futher_room_1 = go_futher_room_1.lower()
                        if go_futher_room_1 == "yes":
                            if "shield" not in inventory:
                                while pickup_shield != "yes" and pickup_shield != "no":
                                    pickup_shield = str(input("You found a shield! Do you want to add it to your inventory? (yes/no): ")) 
                                    pickup_shield.lower()
                                    if pickup_shield == "yes":
                                        inventory.add("shield")
                                        print("                           ")
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
                                        print("*Now this is your inventory:", inventory)
                                        print("                           ")
                                        print("Now the room is empty... return to the main room!")                            
                                    elif pickup_shield == "no":
                                        print("You dont want to improve your defense... ok kid, return to the main room!")                                    
                                    else:
                                        print("Please try again kid, you can only type YES or NO...")
                                pickup_shield = None
                            elif "shield" in inventory:
                                print("Seems like there is nothing here!")
                        elif go_futher_room_1 == "no":
                            print("Ok, return to the main room!")                        
                        else:
                            print("Please try again kid, you can only type YES or NO...")
                    go_futher_room_1 = None
                elif room_1 == "no":
                    print("Ok, return to the main room!")
                else:
                    print("Please try again kid, you can only type YES or NO...")            
            room_1 = None
        elif door_selection == 1 and "sword" in inventory and "shield" in inventory:
            print("---------------------------------")
            print("-                               -")
            print("-                               -")
            print("-                               -")
            print("-  Seems like there is          -")
            print("-  nothing left here..!         -")
            print("-  go back to the main room!    -")
            print("-                               -")
            print("---------------------------------")
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
            
            
            print("    *PRIEST APPEARS*                        ")                      
            print("   .-------.                                ")
            print("  /   -|-   \      _____________________    ")
            print("  |    |    |     /  Do you want my    /    ")
            print("  |   .+.   |    /  bless kid?        /     ")
            print("  | ( o.o ) |   /  On your knees!!   /      ")
            print("  |  |   |  |  /____________________/       ")
            print("  |  |---|  | /                             ")
            print("  |  |___|  |                               ")
            print("  |         |                               ")
            print("  |   / \   |                               ")
            print("  |  (   )  |                               ")
            print("   \-------/                                ")
            print("    | | | |                                 ")
            print("    '-' '-'                                 ")
            print("                                            ")
            print("                                            ")
      
            while get_bless != "kneel" and get_bless != "stand":
                get_bless = str(input("Type: kneel \nType: stand"))

                if get_bless == "kneel":
                    life_points = life_points + 1
                    print("                                                        ")
                    print("      * *      **                                       ")
                    print("    **   **  **  **    ", player," you recived          ")
                    print("   **      **     **      the blessing of the           ")
                    print("  **                **     Gods... use it wisely!       ")
                    print(" **                  **                                 ")
                    print("**       / ^ ^ \      **   *You got +1 Life points      ")
                    print("**      | (o.o) |     **   for a total of:", life_points )
                    print(" **     |   ^   |    **                                 ")
                    print("  **    \  / \ /    **                                  ")
                    print("   **    \/   \/   **                                   ")
                    print("                                                        ")

                    while get_bless != "yes" and fight_dragon != "no":
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