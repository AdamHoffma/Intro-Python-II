from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

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
player = Player('Adam', room['outside'])
# Write a loop that:
while True:
# * Prints the current room name
    print("You are in the {}.".format(player.location.name))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
    print("Enter a direction of travel: n for North, s for South, e for East, and w for West. Press q to quit the game")
# * Waits for user input and decides what to do.
    x = input()
    if(x == 'n'):
        xvalue = player.location.n_to
    elif(x == 's'):
        xvalue = player.location.s_to
    elif(x == 'e'):
        xvalue = player.location.e_to
    elif(x == 'w'):
        xvalue = player.location.w_to
    elif(x == 'q'):
        print("Goodbye")
        break
    else:
        print("Invalid selection")
        continue
    if(xvalue != None):
        player.location = xvalue
    else:
        print("Cannot move in that direction")
        continue

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
