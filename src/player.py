# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name #This is the name of the player
        self.location = location #This is the room the player is currently in

    def change_location(self, new_location):  #For changing locations
        self.location = new_location
