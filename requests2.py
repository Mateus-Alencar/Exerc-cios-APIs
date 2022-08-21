import requests
import json

digimons = requests.get("https://digimon-api.vercel.app/api/digimon")

print(digimons.text)

dict = json.loads(digimons.text)
print(dict[0])
print('##################################################')
for item in dict:
    print(item['name'], item['level'])