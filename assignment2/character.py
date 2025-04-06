import random

class Character:
    def __init__(self, combat_strength=None, health_points=None):
        # Using dice rolls
        self._combat_strength = combat_strength if combat_strength else random.randint(1, 6)
        self._health_points = health_points if health_points else random.randint(1, 20)

    # Getter for combat_strength
    @property
    def combat_strength(self):
        return self._combat_strength

    # Setter for combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        if value < 0:
            raise ValueError("Combat strength cannot be negative")
        self._combat_strength = value

    # Getter for health_points
    @property
    def health_points(self):
        return self._health_points

    # Setter for health_points
    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Health points cannot be negative")
        self._health_points = value

    def __del__(self):
        print("Character object is being destroyed.")