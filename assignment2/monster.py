from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        print("The Monster is being destroyed by the garbage collector")
        super().__del__()

    def monster_attacks(self, hero):
        print(f"Monster attacks! (Strength is: {self.combat_strength})")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Monster has defeated the hero!")
        else:
            hero.health_points -= self.combat_strength
            print(f"Hero's remaining health is: {hero.health_points}")
