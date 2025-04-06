import random

class Character:
    def __init__(self):
        self._combat_strength = random.randint(1, 10)
        self._health_points = random.randint(50, 100)
    
    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value < 0:
            raise ValueError("Combat strength cannot be negative.")
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            self._health_points = 0  # Ensure health doesn't go negative
        else:
            self._health_points = value

    def __del__(self):
        print("Character object is being destroyed by the garbage collector.")
