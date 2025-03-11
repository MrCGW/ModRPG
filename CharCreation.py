#Character creation script.
#First version - name, race, and health.
#Type is the identifier of enemy or player.

import random, json #Combat

def playerC(): #Character creation function.
    character = {}
    print("Welcome to creating your character")
    saved = input("Do you wish to load a saved character? Y or N")
    if saved.strip().lower() == "y":
        with open('Character.json') as json_file: #Open an existing, saved, character
            character = json.load(json_file)
    else:
        name = input("Enter your character's name: ")
        health = random.randint(10,25)
        character.update({"Name" : name})
        character.update({"Health" : health})
    return character

def EnemyC():
    names = ["Ug", "Grok", "Druug", "Varaag"]
    raceLst = ["Orc", "Goblin", "Hobgoblin"]
    EnemyStat = {}
    name = random.choice(names)

    EnemyStat.update({"Name" : name})
    race = random.choice(raceLst)
    EnemyStat.update({"Type": race})
    health = random.randint(5, 20)
    if race == "Orc":
        health += 10
    elif race == "Hobgoblin":
        health += 5
    EnemyStat.update({"Health": health})
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
# Allows picking of a random enemy from the enemy list
AttLst = random.randrange(len(EnemyList))
# AttLst = random.choice(EnemyList)

#print statements for testing
print(len(EnemyList))
print(AttLst)
print(EnemyList[AttLst].get("Name"))

#Future Functionality to import combat.py
#Combat.run_combat(character, enemy)