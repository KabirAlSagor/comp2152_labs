import random

# Hero using loot to adjust health
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("\nUsing your first item from the belt...")
    first_item = belt.pop(0)

    if first_item in good_loot_options:
        health_points = min(20, health_points + 2)
        print(f"You used {first_item} to increase health to {health_points}.")
    elif first_item in bad_loot_options:
        health_points = max(0, health_points - 2)
        print(f"You used {first_item} and lost health. Current health: {health_points}.")
    else:
        print(f"You used {first_item}, but it's not helpful.")

    return belt, health_points

# Hero collecting random loot
def collect_loot(loot_options, belt):
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print(f"You found: {loot}")
    return loot_options, belt

# Simulate dream levels
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)

    if num_dream_lvls == 1:
        print("You are in the deepest dream level.")
        return 2

    # Recursive case
    return 1 + inception_dream(num_dream_lvls - 1)

# Save the game result
# Save the game results to a file (with hero's name if the hero wins)
def save_game(winner, hero_name="Unknown Hero"):
    try:
        with open("save.txt", "a") as file:
            if winner == "Hero":
                file.write(f"Hero {hero_name} has killed a monster.\n")
            else:
                file.write("Monster has defeated the hero.\n")
        print("\nGame progress saved successfully!")
    except Exception as e:
        print(f"Error saving the game: {e}")


# previous game results
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("\n📖 Loading previous game history...")
            lines = file.readlines()

            if not lines:
                print("No previous game records found.")
                return

            hero_wins = [line for line in lines if "Hero" in line]
            monster_wins = [line for line in lines if "Monster" in line]

            print(f"Total monsters killed across all sessions: {len(hero_wins)}")

            if hero_wins:
                print("Heroes who killed monsters:")
                for line in hero_wins:
                    hero_name = line.split("Hero ")[1].split(" has")[0]
                    print(f"- {hero_name}")

            if monster_wins:
                print(f"Times the monster has defeated the hero: {len(monster_wins)}")

    except FileNotFoundError:
        print("No save file found. Starting a fresh game.")
    except Exception as e:
        print(f"❌ Error loading the game: {e}")