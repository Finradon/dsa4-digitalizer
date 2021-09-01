import json

with open('zauber.json') as f:
    data = json.load(f)

spell = data['Balsam']['kosten']
print(spell)