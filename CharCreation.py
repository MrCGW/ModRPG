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

def EnemyC():
    EnemyStat = {}
    race = random.choice(list(Bad_Guys_List.keys()))
    HPMod = Bad_Guys_List[race]
    name = random.choice(race_names[race])
    health = random.randint(5, 20) + HPMod

    EnemyStat.update({"Name" : name})
    EnemyStat.update({"Race": race})
    EnemyStat.update({"Health" : health})

    return EnemyStat

#Creating a list of dictionaries for multiple enemies
EnemyList = []
NoEn = int(input("How many enemies do you want to create?"))
for i in range(NoEn):
    enemy = EnemyC()
    EnemyList.append(enemy)

character = playerC()

print(character)
print(EnemyList)
# Write the PC to a json file
with open('Character.json', 'w') as f:
    json.dump(character, f)


# Generate a random int from 0 to length of list.
# Allows picking of a random enemy from the enemy list - stored in Attr
Attr = random.randrange(len(EnemyList))

#print statements for testing
print(len(EnemyList))
print(Attr)
name, health = EnemyList[Attr].get("Name"), EnemyList[Attr].get("Health")
print(name , health)


#Future Functionality to import combat.py
#Combat.run_combat(character, enemy)