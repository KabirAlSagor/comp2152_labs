from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        print("The Hero is being destroyed by the garbage collector")
        super().__del__()

    def hero_attacks(self, monster):
        print(f"Hero attacks! (Strength is: {self.combat_strength})")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("Hero has defeated the monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"Monster's remaining health is: {monster.health_points}")
