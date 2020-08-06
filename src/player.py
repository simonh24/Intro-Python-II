# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Weapon

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = [Weapon("Wooden Sword", "Flimsy Stick", 1)]
        self.hp = 25
        self.equipped = self.items[0]
    def __str__(self):
        return f"{self.name}\nHP: {self.hp}\n{self.current_room}"
    def heal(self, amt):
        self.hp += amt