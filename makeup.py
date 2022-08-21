import requests
import json

req = requests.get('http://makeup-api.herokuapp.com/api/v1/products.json')
dict = json.loads(req.text)

for produto in dict:
    print(produto['brand'], produto['name'])