from room import Room
from player import Player
from item import Item, Weapon
from monster import Monster

# Declare all the items

item = {
    'rusty_sword': Weapon("Rusty Sword", "A bad rusted sword", 4),
    'potion': Item("Potion", "A high grade potion. Recover 25 HP."),
    'legendary_sword': Weapon("Legendary Sword", "The legendary sword", 15)
}

# Declare monsters

monster = {
    'dummy': Monster('Dummy', 1, 0),
    'zombie': Monster('Zombie', 15, 6),
    'skeleton': Monster('Skeleton', 12, 4),
    'goblin': Monster('Goblin', 8, 2),
    'demon': Monster('Demon', 40, 12)
}

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", [item['rusty_sword'],], monster['dummy']),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [item['potion'],], monster['goblin']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [], monster['zombie']),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! The only exit is to the south.""", [item['legendary_sword'],]),

    'boss_room': Room("Demon's Lair", "The powerful demon residing this cave has been waiting for you. You ready yourself for combat.", [], monster['demon'])
}

# Link rooms together

room['outside'].n_to = room['foyer'] #N
room['foyer'].s_to = room['outside'] #S
room['foyer'].n_to = room['overlook'] #N
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['boss_room']
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

while plyr.hp > 0:
    # print(f"\nCurrent Room: {plyr.current_room.name}")
    # print(f"Current Description: {plyr.current_room.description}")
    # print("Current Room's Items:")
    # for i in plyr.current_room.item:
    #     print(f"\t{i.name}")
    print(plyr)
    if not plyr.current_room.monster == None:
        print("You must fight this monster.")
        print("Pick attack or use (a/u)")
        choice = input("> ")
        if choice == "a":
            plyr.current_room.monster.hp = plyr.current_room.monster.hp - plyr.equipped.att
        elif choice == "u":
            if plyr.items.count(item['potion']) > 0:
                plyr.heal(25)
            else:
                print("You do not have any potions. You must attack.")
                plyr.current_room.monster.hp = plyr.current_room.monster.hp - plyr.equipped.att
        if (plyr.current_room.monster.hp > 0):
            plyr.hp -= plyr.current_room.monster.att
        else:
            print("Monster has been slained")
            plyr.current_room.monster = None
        if plyr.current_room == room['boss_room']:
            if plyr.current_room.monster == None:
                print("You have slain the demon controlling this cave, you win!")
                break
    else:
        print("Where would you like to go?")
        print("-> n for North")
        print("-> s for South")
        print("-> w for West")
        print("-> e for East")
        print("-> i for Inventory")
        print("-> t for Take")
        print("-> d for Drop")
        print("-> q for Quit")
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
            elif plyr.current_room == room["foyer"]:
                plyr.current_room = room["boss_room"]
            else:
                print("You cannot move this direction.")
        elif choice == "e" or choice == "east":
            if plyr.current_room == room["foyer"]:
                plyr.current_room = room["narrow"]
            else:
                print("You cannot move this direction.")
        elif choice == "q" or choice == "quit":
            print("Now quitting...")
            break
        elif choice == "i" or choice == "inventory":
            print("Inventory:")
            for i in range(len(plyr.items)):
                print(f"\n-> {plyr.items[i]}")
        elif choice == "t" or choice == "take" or choice == "get" or choice == "g":
            if len(plyr.current_room.item) == 0:
                print("There is nothing to take")
            else:
                for i in range(len(plyr.current_room.item)):
                    print(f"{i}: {plyr.current_room.item[i].name}")
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
                    new_item = plyr.current_room.item[int(taken)]
                    new_item.on_take()
                    if isinstance(new_item, Weapon):
                        plyr.current_room.item.append(plyr.equipped)
                        plyr.items.remove(plyr.equipped)
                        plyr.equipped = new_item
                    plyr.items.append(plyr.current_room.item.pop(int(taken)))
                except:
                    print("That is not a valid choice, please choose again.")
        elif choice == "d" or choice == "drop":
            if len(plyr.items) == 0:
                print("There is nothing to drop")
            else:
                for i in range(len(plyr.items)):
                    print(f"{i}: {plyr.items[i].name}")
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
                    plyr.items[int(drop)].on_drop()
                    plyr.current_room.item.append(plyr.items.pop(int(drop)))
                except:
                    print("That is not a valid choice, please choose again.")
        else:
            print("That is not a valid choice")
    print("\n-------------------------------------------------------")