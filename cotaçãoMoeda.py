import requests
import json

requisicao =  requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = requisicao.json()

print('###Cotação do dolar######')
print('Moeda: ' + cotacao['USD']['name'])
print('Preço mais alto:' + cotacao['USD']['high'])
print('Preço mais baixo:' + cotacao['USD']['low'])