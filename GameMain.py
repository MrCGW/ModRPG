# GameMain script - the starting point of the game project.

import json
from CharCreation import playerC
from Enemy_Creator import run_enemy
from Combat import run_combat


def begin():
    character = None

    print("Greetings adventurer\n")
    print("Choose and option from the list:\n")
    while character is None:

        print("1 - Create Character\n2 - Load Character\n")
        try:
            option = int(input())
            if option == 1:
                character = playerC()
                return character
            elif option == 2:
                try:
                    with open('Character.json') as json_file:  # Open an existing, saved, character
                        character = json.load(json_file)
                except FileNotFoundError:
                    print("No character file saved. Please create a character first")
            else:
                print("Invalid Choice. Please enter 1 or 2.")
        except ValueError:
            print("Please choose from the list")

    if not character: # makes sure a character is returned.
        print("Error: No character found. Taking you to character creation")
        character = playerC()

    return character

character = begin()
print("Game Main character: ", character)
enemy_list = run_enemy()
print(enemy_list)
run_combat(character, enemy_list)
