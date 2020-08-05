from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

while not choice == "q":
    print(f"Current Room: {plyr.current_room.name}")
    print(f"Current Description: {plyr.current_room.description}")
    print("Where would you like to go? (n, s, w, e) q to quit. ") # need to take input + _to so we can pick directions.
    choice = input("> ")
    if choice == "n":
        if plyr.current_room == room["outside"]:
            plyr.current_room = room["foyer"]
        elif plyr.current_room == room["foyer"]:
            plyr.current_room = room["overlook"]
        elif plyr.current_room == room["narrow"]:
            plyr.current_room = room["treasure"]
        else:
            print("You cannot move this direction.")
    elif choice == "s":
        if plyr.current_room == room["foyer"]:
            plyr.current_room = room["outside"]
        elif plyr.current_room == room["overlook"]:
            plyr.current_room = room["foyer"]
        elif plyr.current_room == room["treasure"]:
            plyr.current_room = room["narrow"]
        else:
            print("You cannot move this direction.")
    elif choice == "w":
        if plyr.current_room == room["narrow"]:
            plyr.current_room = room["foyer"]
        else:
            print("You cannot move this direction.")
    elif choice == "e":
        if plyr.current_room == room["foyer"]:
            plyr.current_room = room["narrow"]
        else:
            print("You cannot move this direction.")
    elif choice == "q":
        print("Now quitting...")
    else:
        print("That is not a valid choice")