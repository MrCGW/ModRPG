# Testing GitHub branch
import random

Bad_Guys_List = {"Umbrakin" : 0, "Drakkaari" : 5, "Ashkith" : 5, "Dreadforged" : 15, "Mireborn" : 10}
race_names = {
    "Umbrakin": ["Nyxveil", "Vorlith the Whisper", "Tenebros", "Shadewraith", "Zyrax the Unseen"],
    "Drakkaari": ["Varkoz the Infernal", "Zyrrak Flamescale", "Molthar the Scorched", "Rhazik Bloodclaw", "Tarkon the Tyrant"],
    "Mireborn": ["Slithmar the Bloated", "Gorvix the Hunger", "Vilethorn", "Ozrath the Swampborn", "Mulgrak the Festering"],
    "Ashkith": ["Zzarkith the Chittering", "Vor'Kaan the Venomous", "Kaathra the Broodmother", "Zykkul the Silent", "Tzorrith the Burrower"],
    "Dreadforged": ["Vorrak the Hollow", "Malrik Ironbane", "Sorrowbrand", "Kaelthorn the Shackled", "Draeven Soulshard"]
}

# checks if the program is run directly or called from another script.
# Explanation - if the script is run directly, the code from below if __name__ will run.
# Otherwise, only the code above will run from the calling program.
if __name__ == "__main__":

    # Stand alone testing for Bad_Guys
    print(Bad_Guys_List)
    # Randomly choose a race from Bad_Guys_List
    # Store the HP modifier for the race
    # Then, based on race chosen randomly get a name
    race = random.choice(list(Bad_Guys_List.keys()))
    HPMod = Bad_Guys_List[race]
    name = random.choice(race_names[race])
    print(race)
    print(HPMod)
    print(name)