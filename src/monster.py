class Monster:
    def __init__(self, monster, hp, att):
        self.monster = monster
        self.hp = hp
        self.att = att
    def __str__(self):
        return f"\n\tMonster Type: {self.monster}\n\tHP: {self.hp}\n\tAttack: {self.att}"