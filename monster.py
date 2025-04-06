from character import Character
import random

class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        damage = random.randint(1, self.combat_strength)
        hero.health_points -= damage
        print(f"Monster attacks Hero for {damage} damage! Hero HP: {hero.health_points}")

    def __del__(self):
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector.")
