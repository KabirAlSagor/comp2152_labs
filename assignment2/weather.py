import random

class WeatherSystem:
    def __init__(self):
        # Initialize weather conditions
        self.weather_conditions = ['rain', 'snow', 'fog', 'clear']
        self.current_weather = random.choice(self.weather_conditions)

    def apply_weather_effects(self, hero):
        """Apply weather effects to the hero."""
        if self.current_weather == 'rain':
            print("It's raining. Your movement is slowed down!")
            hero.combat_strength -= 1  # Example: rain weakens combat strength
        elif self.current_weather == 'snow':
            print("It's snowing. Your movement is slower!")
            hero.combat_strength -= 1  # Example: snow weakens combat strength
        elif self.current_weather == 'fog':
            print("It's foggy. Your visibility is reduced!")
            hero.combat_strength -= 2  # Example: fog reduces combat strength
        else:
            print("The weather is clear. No effects!")
            # No change in stats for clear weather

    def change_weather(self):
        """Randomly change the weather for the next round."""
        self.current_weather = random.choice(self.weather_conditions)
        print(f"The weather has changed to: {self.current_weather}")
