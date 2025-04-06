from character import Character
import random

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.shield_active = False
        self.speed_boost_active = False
        self.double_score_active = False

    def hero_attacks(self, monster):
        damage = random.randint(1, self.combat_strength)
        if self.double_score_active:
            damage *= 2
        monster.health_points -= damage
        print(f"Hero attacks Monster for {damage} damage! Monster HP: {monster.health_points}")
