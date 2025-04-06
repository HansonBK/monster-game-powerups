import random
import os
import platform
from hero import Hero
from monster import Monster

# Print system and Python version information
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

def validate_input():
    while True:
        try:
            level = int(input("Enter dream level (0-3): "))
            if 0 <= level <= 3:
                return level
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 3.")

def use_loot(belt, hero):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]
    
    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        hero.health_points = min(20, (hero.health_points + 2))
        print(f"    |    You used {first_item} to increase your health to {hero.health_points}")
    elif first_item in bad_loot_options:
        hero.health_points = max(0, (hero.health_points - 2))
        print(f"    |    You used {first_item} and lost health to {hero.health_points}")
    else:
        print(f"    |    You used {first_item}, but it's not helpful.")
    return belt

def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously.\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

def adjust_combat_strength(hero, monster):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            print("    |    ... Increasing the monster's combat strength since you won last time.")
            monster.combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            hero.combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time.")