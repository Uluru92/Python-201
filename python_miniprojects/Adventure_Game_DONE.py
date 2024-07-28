#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

#functions:
def get_life_points (life_points: int)-> int:
    """Get an extra +1 life point.
    Args:
        Actual life points (int): Initial life points
    Returns:
        Final life points int(): Total life points
    """
    total_life_points = life_points + 1
    return total_life_points
#Start!
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
print(" ||   |___|   ||       INSTRUCTIONS: Kill the dragon.")
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

import random

door_selection = None

room_1 = None #WHERE YOU CAN FIND A SWORD AND A SHIELD...
go_futher_room_1 = None
pickup_sword = None
pickup_shield = None

room_2 = None
attack_dragon = None

room_3 = None
get_bless = None
power_of_gods = int(0)

inventory = set()
inventory_list = list()
win_chance = int()
battle_result = int()

while door_selection == None:
    door_selection = input("You have to select a door, make a choice: 1|2|3|4|5: ")
    if door_selection not in "12345" or door_selection == "":
        print("Please try again kid, you can only pick a room from the following numbers: 1|2|3|4|5")
    else:
        door_selection = int(door_selection)
        if door_selection == 1:
            if "sword" not in inventory or "shield" not in inventory:
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
                                            pickup_shield = pickup_shield.lower()
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
            elif "sword" in inventory and "shield" in inventory:
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
            print("########################################################")
            print("##                                                    ##")
            print("##        THERE IS A DRAGON SLEEPING HERE...!         ##")
            print("##                                                    ##")
            print("##                  ,-.        ,-.                    ##")
            print("##                 /   \      /   \                   ##")
            print("##                /     \    /     \                  ##")
            print("##              /   .--.  /   .--.  \                 ##")
            print("##             |  /  oo \ | /  oo \  |                ##")
            print("##             | |  ^   | |  ^   | |                  ##")
            print("##             | '--'   '--'   '--' |                 ##")
            print("##             |       |       |       |              ##")
            print("##             |       |       |       |              ##")
            print("##       .--.   |       |       |    .--.             ##")
            print("##      /    \  |   .--.  .--.  |   /    \            ##")
            print("##    /  .--. \ |  /    \  /    \  | /  .--. \        ##")
            print("##    | |    | || |      | |      || |    | |         ##")
            print("##    | |    | || |      | |      || |    | |         ##")
            print("##     \ '--' /  | |   .--.  .--.   |  \ '--' /       ##")
            print("##      \___/    | |  /    \  /    \  |   \___/       ##")
            print("##       '-'        '-'        '-'                    ##")
            print("##                                                    ##")
            print("########################################################")
            while attack_dragon != "yes" and attack_dragon != "no":
                attack_dragon = str(input("Do you want to attack the dragon?(yes/no): "))
                attack_dragon = attack_dragon.lower()
                if attack_dragon == "yes":
                    win_chance = int()
                    inventory_list = list(inventory)
                    if inventory.__len__() == 0:
                        win_chance = 10
                        print("You have",inventory.__len__(),"items in your inventory")
                        print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                ...BATTLE IN PROGRESS....                              ")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                                                                       ")
                        battle_result = random.randint(1,100)
                        if battle_result <= 10:
                            print("YOU KILLED THE DRAGON WITH A PROBABILITY OF",win_chance,"IN A 100")
                            print("YOU ARE ALMOST A GOD, CONGRATZ!", player,"!!!!                   ")
                            exit(0)
                        else:
                            if life_points==2:
                                print("The dragon killed you, but you were blessed with the power ")
                                print("of the GODS! You can start over now!          ")
                                print("You better get some items before trying to kill the dragon!")
                            else:
                                print("The dragon ate you... You lost the game!")
                                exit(0)
                    elif inventory.__len__() == 1:
                        win_chance = 40
                        print("You have",inventory.__len__(),"items in your inventory")
                        print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                ...BATTLE IN PROGRESS....                              ")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                                                                       ")
                        battle_result = random.randint(1,100)
                        if battle_result <= win_chance:
                            print("YOU KILLED THE DRAGON AND WON THE GAME!")
                            print("CONGRAZ", player,"!!!!                 ")
                            exit(0)
                        else:
                            if life_points==2:
                                print("The dragon killed you, but you were blessed with the power ")
                                print("of the GODS, you revived! You can start over now!          ")
                                print("You lost your",inventory_list[0],"!")
                                print("The chances of winning are higher if you get more items!   ")
                                inventory = set()
                            else:
                                print("The dragon ate you... You lost the game!")
                                exit(0)
                    elif inventory.__len__() == 2:
                        win_chance = 80
                        print("You have",inventory.__len__(),"items in your inventory")
                        print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                ...BATTLE IN PROGRESS....                              ")
                        print("                                                                       ")
                        print("                                                                       ")
                        print("                                                                       ")
                        battle_result = random.randint(1,100)
                        if battle_result <= win_chance:
                            print("YOU KILLED THE DRAGON AND WON THE GAME!")
                            print("CONGRAZ", player,"!!!!                 ")
                            exit(0)
                        else:
                            if life_points==2:
                                print("The dragon killed you, but you were blessed with the power ")
                                print("of the GODS! You can start over now!                       ")
                                print("You lost your",inventory_list[0],"and your",inventory_list[1])
                                inventory = set()
                            else:
                                print("The dragon ate you... You lost the game!")
                                exit(0)
                elif attack_dragon == "no":
                    if inventory.__len__() == 0:
                        print("Ok, good choice because you are not prepared to kill the dragon yet! go find a weapon before coming back!")
                    elif inventory.__len__() == 1:
                        print("Ok, good choice because your chances of winning with just",inventory.__len__(),"item are 50%!")
                    elif inventory.__len__() == 2:
                        print("You had great chances of winning, but ok, return to the main room")                    
                else:
                    print("Please, enter 'yes' if you want to fight the dragon, or 'no' if you want to leave the room")
            attack_dragon = None #reset the option to continue to the dragon room in case the player comes back to this room later
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
                get_bless = input("Type: kneel or stand\nYour choice: ")
                get_bless = get_bless.lower()
                if get_bless == "kneel" and power_of_gods == 0:
                    life_points = get_life_points(life_points)
                    print(life_points)
                    power_of_gods = int(power_of_gods)+1
                    print("                                                        ")
                    print("      * *      **                                       ")
                    print("    **   **  **  **    ", player,"...you recived        ")
                    print("   **      **     **      the blessing of the           ")
                    print("  **                **     Gods... use it wisely!       ")
                    print(" **                  **                                 ")
                    print("**       / ^ ^ \      **   *Now you can come back       ")
                    print("**      | (o.o) |     **   from death once!             ")
                    print(" **     |   ^   |    **                                 ")
                    print("  **    \  / \ /    **                                  ")
                    print("   **    \/   \/   **                                   ")
                    print("                          *Now, return to the main room!")               
                elif get_bless == "kneel" and power_of_gods != 0:
                    print("    *PRIEST APPEARS*                        ")                      
                    print("   .-------.                                ")
                    print("  /   -|-   \      _____________________    ")
                    print("  |    |    |     /  I am sorry kid,   /    ")
                    print("  |   .+.   |    /  I can only bless  /     ")
                    print("  | ( o.o ) |   /  you one time!     /      ")
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
                    print("  *Return to the main room                  ")
                elif get_bless == "stand":
                    print("Ok, return to the main room!")               
                else:
                    print("Please try again kid, you can only: keel or stand")
            get_bless = None   
        elif door_selection == 4:
            print("---------------------------------")
            print("-                               -")
            print("-                               -")
            print("-  Seems like there is          -")
            print("-  nothing here..!              -")
            print("-  go back to the main room!    -")
            print("-                               -")
            print("---------------------------------")
        elif door_selection == 5:
            door_selection = random.randint(1,4)
            print("-----------------------------------------")
            print("-                                       -")
            print("-                                       -")
            print("-  You just entered the multiverse!     -")
            print("-  You will be teleported to another    -")
            print("-  room!                                -")
            print("-                                       -")
            print("-----------------------------------------")
            if door_selection == 1:
                print("****....TELEPORTED TO THE ROOM",door_selection)
                if "sword" not in inventory or "shield" not in inventory:
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
                                                pickup_shield = pickup_shield.lower()
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
                elif "sword" in inventory and "shield" in inventory:
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
                print("****....TELEPORTED TO THE ROOM",door_selection)
                print("########################################################")
                print("##                                                    ##")
                print("##        THERE IS A DRAGON SLEEPING HERE...!         ##")
                print("##                                                    ##")
                print("##                  ,-.        ,-.                    ##")
                print("##                 /   \      /   \                   ##")
                print("##                /     \    /     \                  ##")
                print("##              /   .--.  /   .--.  \                 ##")
                print("##             |  /  oo \ | /  oo \  |                ##")
                print("##             | |  ^   | |  ^   | |                  ##")
                print("##             | '--'   '--'   '--' |                 ##")
                print("##             |       |       |       |              ##")
                print("##             |       |       |       |              ##")
                print("##       .--.   |       |       |    .--.             ##")
                print("##      /    \  |   .--.  .--.  |   /    \            ##")
                print("##    /  .--. \ |  /    \  /    \  | /  .--. \        ##")
                print("##    | |    | || |      | |      || |    | |         ##")
                print("##    | |    | || |      | |      || |    | |         ##")
                print("##     \ '--' /  | |   .--.  .--.   |  \ '--' /       ##")
                print("##      \___/    | |  /    \  /    \  |   \___/       ##")
                print("##       '-'        '-'        '-'                    ##")
                print("##                                                    ##")
                print("########################################################")
                while attack_dragon != "yes" and attack_dragon != "no":
                    attack_dragon = str(input("Do you want to attack the dragon?(yes/no): "))
                    attack_dragon = attack_dragon.lower()
                    if attack_dragon == "yes":
                        win_chance = int()
                        inventory_list = list(inventory)
                        if inventory.__len__() == 0:
                            win_chance = 10
                            print("You have",inventory.__len__(),"items in your inventory")
                            print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                ...BATTLE IN PROGRESS....                              ")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                                                                       ")
                            battle_result = random.randint(1,100)
                            if battle_result <= 10:
                                print("YOU KILLED THE DRAGON WITH A PROBABILITY OF",win_chance,"IN A 100")
                                print("YOU ARE ALMOST A GOD, CONGRATZ!", player,"!!!!                   ")
                                exit(0)
                            else:
                                if life_points==2:
                                    print("The dragon killed you, but you were blessed with the power ")
                                    print("of the GODS! You can start over now!          ")
                                    print("You better get some items before trying to kill the dragon!")
                                else:
                                    print("The dragon ate you... You lost the game!")
                                    exit(0)
                        elif inventory.__len__() == 1:
                            win_chance = 40
                            print("You have",inventory.__len__(),"items in your inventory")
                            print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                ...BATTLE IN PROGRESS....                              ")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                                                                       ")
                            battle_result = random.randint(1,100)
                            if battle_result <= win_chance:
                                print("YOU KILLED THE DRAGON AND WON THE GAME!")
                                print("CONGRAZ", player,"!!!!                 ")
                                exit(0)
                            else:
                                if life_points==2:
                                    print("The dragon killed you, but you were blessed with the power ")
                                    print("of the GODS, you revived! You can start over now!          ")
                                    print("You lost your",inventory_list[0],"!")
                                    print("The chances of winning are higher if you get more items!   ")
                                    inventory = set()
                                else:
                                    print("The dragon ate you... You lost the game!")
                                    exit(0)
                        elif inventory.__len__() == 2:
                            win_chance = 80
                            print("You have",inventory.__len__(),"items in your inventory")
                            print("the chances of winning the battle are:", win_chance,"%...Good luck kid!")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                ...BATTLE IN PROGRESS....                              ")
                            print("                                                                       ")
                            print("                                                                       ")
                            print("                                                                       ")
                            battle_result = random.randint(1,100)
                            if battle_result <= win_chance:
                                print("YOU KILLED THE DRAGON AND WON THE GAME!")
                                print("CONGRAZ", player,"!!!!                 ")
                                exit(0)
                            else:
                                if life_points==2:
                                    print("The dragon killed you, but you were blessed with the power ")
                                    print("of the GODS, you revived! You can start over now!          ")
                                    print("You lost your",inventory_list[0],"and your",inventory_list[1])
                                    inventory = set()
                                else:
                                    print("The dragon ate you... You lost the game!")
                                    exit(0)
                    elif attack_dragon == "no":
                        if inventory.__len__() == 0:
                            print("Ok, good choice because you are not prepared to kill the dragon yet! go find a weapon before coming back!")
                        elif inventory.__len__() == 1:
                            print("Ok, good choice because your chances of winning with just",inventory.__len__(),"item are 50%!")
                        elif inventory.__len__() == 2:
                            print("You had great chances of winning, but ok, return to the main room")                    
                    else:
                        print("Please, enter 'yes' if you want to fight the dragon, or 'no' if you want to leave the room")
                attack_dragon = None #reset the option to continue to the dragon room in case the player comes back to this room later
            elif door_selection == 3:
                print("****....TELEPORTED TO THE ROOM",door_selection)        
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
                    get_bless = input("Type: kneel or stand\nYour choice: ")
                    get_bless = get_bless.lower()
                    if get_bless == "kneel" and power_of_gods == 0:
                        life_points = life_points + 1
                        power_of_gods = int(power_of_gods)+1
                        print("                                                        ")
                        print("      * *      **                                       ")
                        print("    **   **  **  **    ", player,"...you recived        ")
                        print("   **      **     **      the blessing of the           ")
                        print("  **                **     Gods... use it wisely!       ")
                        print(" **                  **                                 ")
                        print("**       / ^ ^ \      **   *Now you can come back       ")
                        print("**      | (o.o) |     **   from death once!             ")
                        print(" **     |   ^   |    **                                 ")
                        print("  **    \  / \ /    **                                  ")
                        print("   **    \/   \/   **                                   ")
                        print("                          *Now, return to the main room!")               
                    elif get_bless == "kneel" and power_of_gods != 0:
                        print("    *PRIEST APPEARS*                        ")                      
                        print("   .-------.                                ")
                        print("  /   -|-   \      _____________________    ")
                        print("  |    |    |     /  I am sorry kid,   /    ")
                        print("  |   .+.   |    /  I can only bless  /     ")
                        print("  | ( o.o ) |   /  you one time!     /      ")
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
                        print("  *Return to the main room                  ")
                    elif get_bless == "stand":
                        print("Ok, return to the main room!")               
                    else:
                        print("Please try again kid, you can only: keel or stand")
                get_bless = None   
            elif door_selection == 4:
                print("****....TELEPORTED TO THE ROOM",door_selection)
                print("---------------------------------")
                print("-                               -")
                print("-                               -")
                print("-  Seems like there is          -")
                print("-  nothing here..!              -")
                print("-  go back to the main room!    -")
                print("-                               -")
                print("---------------------------------")
    door_selection = None