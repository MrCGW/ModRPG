import random

Bad_Guys_List = ["Umbrakin", "Drakkaari", "Ashkith", "Dreadforged", "Mireborn"]
race_names = {
    "Umbrakins": ["Nyxveil", "Vorlith the Whisper", "Tenebros", "Shadewraith", "Zyrax the Unseen"],
    "Drakkari": ["Varkoz the Infernal", "Zyrrak Flamescale", "Molthar the Scorched", "Rhazik Bloodclaw", "Tarkon the Tyrant"],
    "Mireborn": ["Slithmar the Bloated", "Gorvix the Hunger", "Vilethorn", "Ozrath the Swampborn", "Mulgrak the Festering"],
    "Ashkith": ["Zzarkith the Chittering", "Vor'Kaan the Venomous", "Kaathra the Broodmother", "Zykkul the Silent", "Tzorrith the Burrower"],
    "Dreadforged": ["Vorrak the Hollow", "Malrik Ironbane", "Sorrowbrand", "Kaelthorn the Shackled", "Draeven Soulshard"]
}


if __name__ == "__main__": #checks if the program is run directly or called from another script
    print(Bad_Guys_List)
    # Randomly choose a race from the list
    # Then, based on race chosen randomly get a name
    race = random.choice(Bad_Guys_List)
    name = random.choice(race_names[race])