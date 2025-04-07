import random
import os
import platform
from hero import Hero
from monster import Monster
import functions  # Use the provided helper functions
from weather import WeatherSystem  # Import the weather system

# Display system information
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Loading previous game state
functions.load_game()

# Creating Hero and Monster objects
hero = Hero()
monster = Monster()

# Initialize the weather system
weather = WeatherSystem()

# Displaying initial stats of Hero and Monster
print(f"Hero's Combat Strength is: {hero.combat_strength}, Health is: {hero.health_points}")
print(f"Monster's Combat Strength is: {monster.combat_strength}, Health is: {monster.health_points}")

# Apply weather effects on Hero
weather.apply_weather_effects(hero)

# Rolling for Weapon
input("Roll the dice for weapon (Press Enter)")
weapon_roll = random.randint(1, 6)
hero.combat_strength += weapon_roll
print(f"Hero's weapon is {weapon_roll}. Updated Combat Strength: {hero.combat_strength}")

# Validate Dream Levels (with exception handling)
num_dream_lvls = -1
while num_dream_lvls < 0 or num_dream_lvls > 3:
    try:
        num_dream_lvls = int(input("Enter dream levels (0-3): "))
        if num_dream_lvls < 0 or num_dream_lvls > 3:
            raise ValueError("Number must be between 0 and 3.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

if num_dream_lvls > 0:
    hero.health_points -= 1
    crazy_level = functions.inception_dream(num_dream_lvls)
    hero.combat_strength += crazy_level
    print(f"Updated Combat Strength is: {hero.combat_strength}")
    print(f"Updated Health Points is: {hero.health_points}")

# Collecting Loot (again)
print("You find a loot bag with two items!")
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

for _ in range(2):
    input("Roll for loot (Press Enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)

# Using the loot
belt, hero.health_points = functions.use_loot(belt, hero.health_points)
print(f"Hero's Health after using loot is: {hero.health_points}")

# Hero vs Monster
print("\n🚀 The battle begins! 🚀")
while hero.health_points > 0 and monster.health_points > 0:
    input("Press Enter to roll for attack...")

    # Apply weather effects during the battle
    weather.apply_weather_effects(hero)

    attack_roll = random.choice(range(1, 7))

    if attack_roll % 2 == 0:
        print("The Monster strikes first!")
        monster.monster_attacks(hero)
    else:
        print("The Hero strikes first!")
        hero.hero_attacks(monster)

    # Change the weather condition after each round
    weather.change_weather()

# Announce the Winner
if hero.health_points > 0:
    print("\n🎉 Hero wins the battle! 🎉")
    winner = "Hero"
else:
    print("\n💀 Monster wins the battle! 💀")
    winner = "Monster"

# Saving game results
hero_name = input("Enter your Hero's name: ")
functions.save_game(winner, hero_name)
