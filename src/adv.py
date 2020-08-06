from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["Rusty Sword"]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", ["Potion"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", ["Legendary Sword"]),
}


# Link rooms together

room['outside'].n_to = room['foyer'] #N
room['foyer'].s_to = room['outside'] #S
room['foyer'].n_to = room['overlook'] #N
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer'] #S
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure'] #N
room['treasure'].s_to = room['narrow'] #S

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
plyr = Player("Simon", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
choice = ""

while not (choice == "q" or choice == "quit"):
    print(f"\nCurrent Room: {plyr.current_room.name}")
    print(f"Current Description: {plyr.current_room.description}")
    print(f"Current Room Items: {plyr.current_room.item}")
    print("Where would you like to go?")
    print("n for North")
    print("s for South")
    print("w for West")
    print("e for East")
    print("i for Inventory")
    print("t for Take")
    print("d for Drop")
    print("q for Quit")
    choice = input("> ")
    choice = choice.lower()
    if choice == "n" or choice == "north":
        if plyr.current_room == room["outside"]:
            plyr.current_room = room["foyer"]
        elif plyr.current_room == room["foyer"]:
            plyr.current_room = room["overlook"]
        elif plyr.current_room == room["narrow"]:
            plyr.current_room = room["treasure"]
        else:
            print("You cannot move this direction.")
    elif choice == "s" or choice == "south":
        if plyr.current_room == room["foyer"]:
            plyr.current_room = room["outside"]
        elif plyr.current_room == room["overlook"]:
            plyr.current_room = room["foyer"]
        elif plyr.current_room == room["treasure"]:
            plyr.current_room = room["narrow"]
        else:
            print("You cannot move this direction.")
    elif choice == "w" or choice == "west":
        if plyr.current_room == room["narrow"]:
            plyr.current_room = room["foyer"]
        else:
            print("You cannot move this direction.")
    elif choice == "e" or choice == "east":
        if plyr.current_room == room["foyer"]:
            plyr.current_room = room["narrow"]
        else:
            print("You cannot move this direction.")
    elif choice == "q" or choice == "quit":
        print("Now quitting...")
    elif choice == "i" or choice == "inventory":
        print(plyr.items)
    elif choice == "t" or choice == "take":
        if len(plyr.current_room.item) == 0:
            print("There is nothing to take")
        else:
            for i in range(len(plyr.current_room.item)):
                print(f"{i}: {plyr.current_room.item[i]}")
            print("Type the number of the item that you would like")
            print("Enter b to go back")
            taken = input("> ")
            while taken == "":
                print("Please pick a choice")
                taken = input("> ")
                taken = taken.lower()
            if taken == "b" or taken == "back":
                print("Taking you back to the room menu...")
            try:
                plyr.items.append(plyr.current_room.item.pop(int(taken)))
            except:
                print("An error has occured.")
    elif choice == "d" or choice == "drop":
        if len(plyr.items) == 0:
            print("There is nothing to drop")
        else:
            for i in range(len(plyr.items)):
                print(f"{i}: {plyr.items[i]}")
            print("Type the number of the item that you would like to drop: ")
            print("Enter b to go back")
            drop = input("> ")
            while drop == "":
                print("Please pick a choice")
                drop = input("> ")
                drop = drop.lower()
            if drop == "b" or drop == "back":
                print("Taking you back to the room menu...")
            try:
                plyr.current_room.item.append(plyr.items.pop(int(drop)))
            except:
                print("An error has occured.")
    else:
        print("That is not a valid choice")