import requests

url = "https://akabab.github.io/superhero-api/api//all.json"
resp = requests.get(url).json()
super_dict = {}
for i in resp:
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    intelligence = 0
    if i['name'] in superheroes and i['powerstats']['intelligence'] > intelligence:
        smartest = i['name']
        intelligence = i['powerstats']['intelligence']
print(f'Из трёх супергероев - {", ".join(superheroes)}, самый умный: {smartest}')