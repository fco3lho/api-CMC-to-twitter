from requests import Request, Session
import json
import pprint
import os
import datetime

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters_btc = {
    'slug': 'bitcoin',
    'convert': 'BRL'
}

parameters_eth = {
    'slug': 'ethereum',
    'convert': 'BRL'
}

parameters_bnb = {
    'slug': 'binance-coin',
    'convert': 'BRL'
}

parameters_ada = {
    'slug': 'cardano',
    'convert': 'BRL'
}

parameters_xpr = {
    'slug': 'xrp',
    'convert': 'BRL'
}

parameters_doge = {
    'slug': 'dogecoin',
    'convert': 'BRL'
}

parameteres_dot = {
    'slug': 'polkadot-new',
    'convert': 'BRL'
}

parameters_icp = {
    'slug': 'internet-computer',
    'convert': 'BRL'
}

parameters_link = {
    'slug': 'chainlink',
    'convert': 'BRL'
}

parameters_usd = {
    'slug': 'tether',
    'convert': 'BRL'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4b3f6d13-e0ad-4400-816f-ba8a0a4af7b4'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params = parameters_btc)
print("Bitcoin price:", json.loads(response.text)['data']['1']['quote']['BRL']['price'])

response = session.get(url, params = parameters_eth)
print("Ethereum price:", json.loads(response.text)['data']['1027']['quote']['BRL']['price'])

response = session.get(url, params = parameters_bnb)
pprint.pprint(json.loads(response.text)['data']['1839']['quote']['BRL']['price'])

response = session.get(url, params = parameters_ada)
pprint.pprint(json.loads(response.text)['data']['2010']['quote']['BRL']['price'])

response = session.get(url, params = parameters_xpr)
pprint.pprint(json.loads(response.text)['data']['52']['quote']['BRL']['price'])

response = session.get(url, params = parameters_doge)
pprint.pprint(json.loads(response.text)['data']['74']['quote']['BRL']['price'])

response = session.get(url, params = parameteres_dot)
pprint.pprint(json.loads(response.text)['data']['6636']['quote']['BRL']['price'])

response = session.get(url, params = parameters_icp)
pprint.pprint(json.loads(response.text)['data']['8916']['quote']['BRL']['price'])

response = session.get(url, params = parameters_link)
pprint.pprint(json.loads(response.text)['data']['1975']['quote']['BRL']['price'])

response = session.get(url, params = parameters_usd)
pprint.pprint(json.loads(response.text)['data']['825']['quote']['BRL']['price'])

