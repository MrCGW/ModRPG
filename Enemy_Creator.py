# Enemy Creation script

import random
import json
from Bad_Guys import Bad_Guys_List, race_names

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

def run_enemy():
    # Creates the number of enemies specified from user input.
    # Creating a list of dictionaries for multiple enemies
    EnemyList = []
    NoEn = int(input("How many enemies do you want to create?"))
    for i in range(NoEn):
        enemy = EnemyC()
        EnemyList.append(enemy)
    with open('EnemyList.json', 'w') as f:
        json.dump(EnemyList, f)
    return EnemyList


    # Generate a random int from 0 to length of list.
    # Allows picking of a random enemy from the enemy list - stored in Attr
    Attr = random.randrange(len(EnemyList))

    #print statements for testing
    #print(len(EnemyList))
    #print(Attr)
    name, health = EnemyList[Attr].get("Name"), EnemyList[Attr].get("Health")
    print(name , health)
    EnemyList.pop(Attr)
    print(EnemyList)

if __name__ == "__main__":
    run_enemy()