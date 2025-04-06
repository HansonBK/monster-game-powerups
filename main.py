from hero import Hero
from monster import Monster
from functions import use_loot, save_game, load_game, adjust_combat_strength
import random
import time

power_up_types = ["Speed Boost", "Shield", "Double Score"]

def spawn_power_up():
    # 30% chance to spawn a power-up
    if random.random() < 0.3:
        return random.choice(power_up_types)
    return None

def activate_power_up(power_up, hero):
    print(f"    |    Activated Power-Up: {power_up}!")
    if power_up == "Shield":
        hero.shield_active = True
    elif power_up == "Speed Boost":
        hero.speed_boost_active = True
    elif power_up == "Double Score":
        hero.double_score_active = True

def main():
    hero = Hero()
    monster = Monster()
    belt = ["Health Potion", "Poison Potion"]
    power_up_inventory = []

    adjust_combat_strength(hero, monster)
    print("Battle begins!")
    belt = use_loot(belt, hero)

    while hero.health_points > 0 and monster.health_points > 0:
        # Chance to spawn power-up
        power_up = spawn_power_up()
        if power_up:
            print(f"    |    A {power_up} appeared!")
            collect = input("    |    Do you want to collect it? (y/n): ").lower()
            if collect == 'y':
                power_up_inventory.append(power_up)
                print(f"    |    {power_up} added to your inventory.")

        # Check if player wants to activate a power-up
        if power_up_inventory:
            use = input(f"    |    Your inventory: {power_up_inventory}. Activate one? (y/n): ").lower()
            if use == 'y':
                chosen = input(f"    |    Enter power-up name: ")
                if chosen in power_up_inventory:
                    activate_power_up(chosen, hero)
                    power_up_inventory.remove(chosen)

        # Hero attacks
        hero.hero_attacks(monster)
        if monster.health_points <= 0:
            print("Monster defeated!")
            save_game("Hero", "Player", 3 if hero.double_score_active else 1)
            break

        # Monster attacks (shield check)
        if not hero.shield_active:
            monster.monster_attacks(hero)
        else:
            print("    |    Shield absorbed the monster's attack!")
            hero.shield_active = False

        if hero.health_points <= 0:
            print("Hero defeated! Game over.")
            save_game("Monster")
            break

        # Reset temporary power-ups
        hero.double_score_active = False
        hero.speed_boost_active = False

    # Display kill count
    with open("save.txt", "r") as file:
        lines = file.readlines()
        print(f"Total monsters killed: {len([line for line in lines if 'Hero' in line])}")

if __name__ == "__main__":
    main()
