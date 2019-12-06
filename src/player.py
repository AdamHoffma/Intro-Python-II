# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name #This is the name of the player
        self.location = location #This is the room the player is currently in
        self.items = []

    def check_inventory(self):
        if len(self.items) > 0:
            all_items = ", ".join([str(item) for item in self.items])
        else:
            all_items = "nothing"
        print(f"Your inventory contains {all_items}.")

    def drop_item(self, item):
        self.items = list(filter(lambda i: not i.name is item.name, self.items))

    def drop_items(self, item):
        self.items.append(item)

    