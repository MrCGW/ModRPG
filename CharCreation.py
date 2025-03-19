# Character creation script.
# See GitHub commits for changes


import random, json
from Weapons import weapon
from Bad_Guys import Bad_Guys_List, race_names

def playerC(): #Character creation function.
    character = {}
    print("### Character Creation ###")
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
    # Write the PC to a json file
    with open('Character.json', 'w') as f:
        json.dump(character, f)
    return character



#character = playerC()

#print(character)




if __name__ == "__main__":
    TestPlayer = playerC()
    print(TestPlayer)


#Future Functionality to import combat.py
#Combat.run_combat(character, enemy)