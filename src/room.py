# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=None):
        self.name = name #This is name of room
        self.description = description #This is description of room
        self.items = None #These are the items in a room

    def print_items(self):
        if len(self.item) > 0:
            all_items= ", ".join([str(item) for item in self.item])
        else:
            all_items = "nothing"
        print(f"You look around the {self.name} and see {all_items}.")

