from requests import Request, Session
import json
import tweepy
import os
import datetime
import time
import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters_btc = {
    'slug': 'bitcoin',
    'convert': 'USD'
}

parameters_eth = {
    'slug': 'ethereum',
    'convert': 'USD'
}

parameters_bnb = {
    'slug': 'binance-coin',
    'convert': 'USD'
}

parameters_ada = {
    'slug': 'cardano',
    'convert': 'USD'
}

parameters_xpr = {
    'slug': 'xrp',
    'convert': 'USD'
}

parameters_doge = {
    'slug': 'dogecoin',
    'convert': 'USD'
}

parameteres_dot = {
    'slug': 'polkadot-new',
    'convert': 'USD'
}

parameters_icp = {
    'slug': 'internet-computer',
    'convert': 'USD'
}

parameters_link = {
    'slug': 'chainlink',
    'convert': 'USD'
}

parameters_usd = {
    'slug': 'tether',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4b3f6d13-e0ad-4400-816f-ba8a0a4af7b4'
}

session = Session()
session.headers.update(headers)

while True:

#'percent_change_24h'

    response = session.get(url, params = parameters_btc)
    price_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    change_24h_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['percent_change_24h'])
    print('BTC: ${:.2f}'.format(price_btc),' |  Change 24h: {:.2f}'.format(change_24h_btc) + '%')

    response = session.get(url, params = parameters_eth)
    price_eth = float(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
    change_24h_eth = float(json.loads(response.text)['data']['1027']['quote']['USD']['percent_change_24h'])
    print('ETH: ${:.2f}'.format(price_eth),'  |  Change 24h: {:.2f}'.format(change_24h_eth)+'%')

    response = session.get(url, params = parameters_bnb)
    price_bnb = float(json.loads(response.text)['data']['1839']['quote']['USD']['price'])
    change_24h_bnb = float(json.loads(response.text)['data']['1839']['quote']['USD']['percent_change_24h'])
    print('BNB: ${:.2f}'.format(price_bnb),'   |  Change 24h: {:.2f}'.format(change_24h_bnb)+'%')

    response = session.get(url, params = parameters_ada)
    price_ada = float(json.loads(response.text)['data']['2010']['quote']['USD']['price'])
    change_24h_ada = float(json.loads(response.text)['data']['2010']['quote']['USD']['percent_change_24h'])
    print('ADA: ${:.2f}'.format(price_ada),'     |  Change 24h: {:.2f}'.format(change_24h_ada)+'%')

    response = session.get(url, params = parameters_xpr)
    price_xrp = float(json.loads(response.text)['data']['52']['quote']['USD']['price'])
    change_24h_xrp = float(json.loads(response.text)['data']['52']['quote']['USD']['percent_change_24h'])
    print('XRP: ${:.2f}'.format(price_xrp),'     |  Change 24h: {:.2f}'.format(change_24h_xrp)+'%')

    response = session.get(url, params = parameters_doge)
    price_doge = float(json.loads(response.text)['data']['74']['quote']['USD']['price'])
    change_24h_doge = float(json.loads(response.text)['data']['74']['quote']['USD']['percent_change_24h'])
    print('DOGE: ${:.2f}'.format(price_doge),'    |  Change 24h: {:.2f}'.format(change_24h_doge)+'%')

    response = session.get(url, params = parameteres_dot)
    price_dot = float(json.loads(response.text)['data']['6636']['quote']['USD']['price'])
    change_24h_dot = float(json.loads(response.text)['data']['6636']['quote']['USD']['percent_change_24h'])
    print('DOT: ${:.2f}'.format(price_dot),'    |  Change 24h: {:.2f}'.format(change_24h_dot)+'%')

    response = session.get(url, params = parameters_icp)
    price_icp = float(json.loads(response.text)['data']['8916']['quote']['USD']['price'])
    change_24h_icp = float(json.loads(response.text)['data']['8916']['quote']['USD']['percent_change_24h'])
    print('ICP: ${:.2f}'.format(price_icp),'   |  Change 24h: {:.2f}'.format(change_24h_icp)+'%')

    response = session.get(url, params = parameters_link)
    price_link = float(json.loads(response.text)['data']['1975']['quote']['USD']['price'])
    change_24h_link = float(json.loads(response.text)['data']['1975']['quote']['USD']['percent_change_24h'])
    print('LINK: ${:.2f}'.format(price_link),'   |  Change 24h: {:.2f}'.format(change_24h_link)+'%')

    # response = session.get(url, params = parameters_usd)
    # price_usd = float(json.loads(response.text)['data']['825']['quote']['USD']['price'])
    # change_24h_usd = float(json.loads(response.text)['data']['825']['quote']['USD']['percent_change_24h'])
    # print('Tether: ${:.2f}'.format(price_usd),'|  Change 24h: {:.2f}'.format(change_24h_usd)+'%')

    time.sleep(60)
    os.system('cls')

