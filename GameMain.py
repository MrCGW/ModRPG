import json
from CharCreation import playerC
from Enemy_Creator import run_enemy
from Combat import run_combat

character = None

print("Greetings adventurer\n")
print("Choose and option from the list:\n")
while character is None:

    print("1 - Create Character\n2 - Load Character\n")
    try:
        option = int(input())
        if option == 1:
            character = playerC()
        elif option == 2:
            try:
                with open('Character.json') as json_file:  # Open an existing, saved, character
                    character = json.load(json_file)
            except FileNotFoundError:
                print("No character file saved")
        else:
            print("Invalid Choice. Please enter 1 or 2.")
    except ValueError:
        print("Please choose from the list")

print("Game Main character: ", character)
enemy_list = run_enemy()
print(enemy_list)
run_combat(character, enemy_list)
