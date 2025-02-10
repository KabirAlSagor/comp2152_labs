import random

def collect_loot(belt, loot_options):
    print("Collecting loot...")
    belt.extend(loot_options)
    return belt, loot_options

def use_loot(belt, health_points):
    if belt:
        item = belt.pop(0)
        print(f"Using {item}...")
        health_points += 5
    return belt, health_points

def inception_dream(crazy_level=0):
    choice = input("Do you want to go deeper into the dream? (yes/no): ").strip().lower()
    if choice == 'yes':
        return inception_dream(crazy_level + 1)
    return crazy_level + 2

# Get hero's name with validation
while True:
    hero_name = input("Enter your Hero's name (in two words): ")
    name_parts = hero_name.split()
    if len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        break
    print("Invalid name! Please enter exactly two words with only letters.")

first_name, second_name = name_parts
short_name = first_name[:2] + second_name[:1]

# Simulating loot collection and usage
belt = []
loot_options = ["Sword", "Shield", "Potion"]
belt, loot_options = collect_loot(belt, loot_options)

health_points = 100
belt, health_points = use_loot(belt, health_points)

# Determine who attacks first
attack_roll = random.randint(1, 6)
if attack_roll in [1, 3, 5]:
    print(f"Hero {short_name} attacks first!")
else:
    print("Monster attacks first!")

# Inception dream sequence
crazy_level = inception_dream()
health_points -= 1  # Reduce health after dream
combat_strength = crazy_level  # Increase combat strength

# Display final status
print(f"Hero {short_name} gets {crazy_level} extra combat strength!")
print(f"Hero's health: {health_points}")
print(f"Hero's belt contains: {', '.join(belt) if belt else 'No items'}")
