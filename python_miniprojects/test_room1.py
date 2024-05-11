door_selection = None


while door_selection == None:
    door_selection = input("select: 1 2 3 4 5: ")
    print(type(door_selection))
    if door_selection not in "12345":
        print("Please try again")
        print(door_selection)
    else:
        door_selection = int(door_selection)
        if door_selection == 1:
            print("door 1")
        elif door_selection == 2:
            print("door 2")
        elif door_selection == 3:
            print("door 3")
        elif door_selection == 4:
            print("door 4")
        elif door_selection == 5:
            print("door 5")
    door_selection = None