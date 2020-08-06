class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"You have taken {self.name}")
    def on_drop(self):
        print(f"You have dropped {self.name}")
    def __str__(self):
        return f"\n\tName: {self.name}\n\tDescription: {self.description}"
    def __repr__(self):
        return self.__str__()

class Weapon(Item):
    def __init__(self, name, description, att):
        self.att = att
        super().__init__(name, description)
    def __str__(self):
        return f"\n\tName: {self.name}\n\tDescription: {self.description}\n\tAttack: {self.att}"
    def __repr__(self):
        return self.__str__()