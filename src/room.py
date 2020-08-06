# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item = [], monster = None):
        self.name = name
        self.description = description
        self.monster = monster
        self.item = item;
    def __str__(self):
        return f"Room Name: {self.name}\nRoom Description: {self.description}\nItems in Room: {self.item}\nMonster in Room: {self.monster}"