#
#Building an RPG - purpose, demonstrating programming skills to students.
#Filename: Combat.py
#Created 10 Mar 2025
#
import random
#Function declarations

#attack function is a D6 roll
def attack():
    hit = random.randint(1,6)
    print(hit)
    if hit%2 == 0:
        return True
    else:
        return False

#Damage - D10 roll
def damage():
    return random.randint(1,10)

def HPCalc(dmg, HP):
     return HP - dmg

#Fight - press enter to attack, calls the functions as required, returns the health value to the main run_combat()
def fight(Health):
    while True:
        input("Press enter to attack")
        success = attack()
        if success:
            print("A hit!")
            dmg = damage()
            print("Damage: ", dmg,"!")
            Health = HPCalc(dmg, Health)
            break
        else:
            print("Miss!")
            break
    return Health

def run_combat(character, enemy): #main function
    PHealth = character.get("Health")
    EHealth = enemy.get("Health")
    PAttack = 0
    EAttack = 0
    print(" &&&&& RPG Combat &&&&& ")
    print("Start of combat your Health = ", PHealth)
    while PHealth > 0 and EHealth > 0: #and logic to see if character is defeated.
        PAttack = PAttack + 1
        print("Your attack", PAttack)
        #Character = "player"
        print("Enemy health: ", EHealth)
        EHealth = fight(EHealth)
        if EHealth <= 0:
            print("Enemy has been defeated")
            break

        #Character = "Enemy"
        print("Enemy attacks you")
        EAttack = EAttack + 1
        print("\nEnemy attack ", EAttack)
        print("Your health: ", PHealth)
        PHealth = fight(PHealth)
        if PHealth <= 0:
            print("You have been defeated")
            break

    print("Combat simulation over!")

if __name__ == "__main__": #checks if the program is run directly or called from another script
    run_combat()