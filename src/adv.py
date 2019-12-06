from room import Room
from player import Player
from item import Item
import colorama
from colorama import Fore, Back, Style

# Declare all items

item = {
    'outside': [Item("torch", "This might help illuminate your way"), Item("shovel", "This might come in handy if you need to dig you way out or hit someone... or thing")],
    'foyer': [Item("ladder", "This could be used to bridge the gap, sadly it's broken")], 
    'overlook': [Item("hammer", "This could be used to fix the ladder, sadly it's broken")],
    'narrow': [Item("water", "A simple glass of water, I wouldn't drink it")],    
    'treasure': [Item("chest", "A treasure chest full of jewels and gold coins, I would definitely take it")]
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons",
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
),
}


# Link rooms together

room['outside'].items = item['outside']
room['foyer'].items = item['foyer']
room['overlook'].items = item['overlook']
room['narrow'].items = item['narrow']
room['treasure'].items = item['treasure']

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Please enter player name")
print()
player = Player(name, room['outside'])
stalwart = Item(item['outside'], room['outside'])
print(stalwart.name.description)
print(f"Welcome, {name}")
# Write a loop that:
while True:
# * Prints the current room name
    
    print("Hi {}! You are in the {}.".format(name, player.location.name))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
    
    print("{} Enter a direction of travel: n for North, s for South, e for East, and w for West. Press q to quit the game".format(name))
# * Waits for user input and decides what to do.
    x = input("Where would you like to go?")
    print()
    if (len(x) == 1):
        if(not (x in ['n', 's', 'e', 'w', 'q'])):
            print(f'    {x} is not an option, try another')
        elif (x == 'n'):
            try:
                player.location = player.location.n_to
            except AttributeError:
                print(f'    {name} cannot move north, try another direction')
        elif (x == 's'):
            try:
                player.location = player.location.s_to
            except AttributeError:
                print(f'    {name} cannot move south, try another direction')
        elif (x == 'w'):
            try:
                player.location = player.location.w_to
            except AttributeError:
                print(f'    {name} cannot move west, try another direction')
        elif (x == 'e'):
            try:
                player.location = player.location.e_to
            except AttributeError:
                    print(f'     {name} cannot move east, try another direction')
        elif (x == "q"):
            print(f'    Goodbye {name}!!')
            break

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
