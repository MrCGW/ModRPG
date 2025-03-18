# Character creation script.
# See GitHub commits for changes


import random, json
from Weapons import weapon
from Bad_Guys import Bad_Guys_List, race_names

def playerC(): #Character creation function.
    character = {}
    print("Welcome to creating your character")
    saved = input("Do you wish to load a saved character? Y or N")
    if saved.strip().lower() == "y":
        try:
            with open('Character.json') as json_file: #Open an existing, saved, character
                character = json.load(json_file)
        except:
            print("No character file saved")
    else:
        name = input("Enter your character's name: ")
        health = random.randint(10,25)
        character.update({"Name" : name})
        character.update({"Health" : health})
        print(weapon)
        weapn = input("Choose a weapon from the list")
        if weapn in weapon:
            print(f"\nYou chose the {weapn}, with {weapon[weapn]} damage")
            character["weapon"]=weapn
            character["Damage"]=weapon[weapn]

    return character



character = playerC()

print(character)

# Write the PC to a json file
with open('Character.json', 'w') as f:
    json.dump(character, f)





#Future Functionality to import combat.py
#Combat.run_combat(character, enemy)