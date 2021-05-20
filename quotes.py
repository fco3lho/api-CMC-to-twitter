from requests import Request, Session
import json
import tweepy
import os
import datetime
import time

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

while True:

    response = session.get(url, params = parameters_btc)
    price_btc = float(json.loads(response.text)['data']['1']['quote']['BRL']['price'])
    print('Bitcoin: R${:.2f}'.format(price_btc))

    response = session.get(url, params = parameters_eth)
    price_eth = float(json.loads(response.text)['data']['1027']['quote']['BRL']['price'])
    print('Ethereum: R${:.2f}'.format(price_eth))

    response = session.get(url, params = parameters_bnb)
    price_bnb = float(json.loads(response.text)['data']['1839']['quote']['BRL']['price'])
    print('Binance Coin: R${:.2f}'.format(price_bnb))

    response = session.get(url, params = parameters_ada)
    price_ada = float(json.loads(response.text)['data']['2010']['quote']['BRL']['price'])
    print('Cardano: R${:.2f}'.format(price_ada))

    response = session.get(url, params = parameters_xpr)
    price_xrp = float(json.loads(response.text)['data']['52']['quote']['BRL']['price'])
    print('Ripple: R${:.2f}'.format(price_xrp))

    response = session.get(url, params = parameters_doge)
    price_doge = float(json.loads(response.text)['data']['74']['quote']['BRL']['price'])
    print('Dogecoin: R${:.2f}'.format(price_doge))

    response = session.get(url, params = parameteres_dot)
    price_dot = float(json.loads(response.text)['data']['6636']['quote']['BRL']['price'])
    print('Polkadot: R${:.2f}'.format(price_dot))

    response = session.get(url, params = parameters_icp)
    price_icp = float(json.loads(response.text)['data']['8916']['quote']['BRL']['price'])
    print('Internet Computer: R${:.2f}'.format(price_icp))

    response = session.get(url, params = parameters_link)
    price_link = float(json.loads(response.text)['data']['1975']['quote']['BRL']['price'])
    print('Chainlink: R${:.2f}'.format(price_link))

    response = session.get(url, params = parameters_usd)
    price_usd = float(json.loads(response.text)['data']['825']['quote']['BRL']['price'])
    print('Tether: R${:.2f}'.format(price_usd))

    time.sleep(60)
    os.system('cls')

