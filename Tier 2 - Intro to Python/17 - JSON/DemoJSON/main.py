import json

with open('Tier 2/17 - JSON/DemoJSON/Stats.json') as stats:
    data = json.load(stats)
    print(data)
    
Strength = input("How much strength? ")
data["Strength: "] = Strength
Constitution = input("How much constituion? ")
data["Constitution: "] = Constitution
Dexterity = input("How much Dexterity? ")
data["Dexterity: "] = Dexterity
Intelligence = input("How much Intelligence? ")
data["Intelligence: "] = Intelligence
Wisdom = input("How much Wisdom? ")
data["Wisdom: "] = Wisdom
Charisma = input("How much Charisma? ")
data["Charisma: "] = Charisma
print(data)