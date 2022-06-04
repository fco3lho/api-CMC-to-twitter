from requests import Request, Session
import json
import tweepy
import os
import datetime
import time

while True: #This 'while' was previously implemented only where the price capture 
            #variables are located, but for long time 'time.sleep()', the data 
            #became idle and was lost, so it was necessary to use it at the 
            # beginning of every interaction with the APIs.
    try: 
        
        # API COINMARKETCAP
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

        parameters_icp = {
            'slug': 'internet-computer',
            'convert': 'USD'
        }

        parameters_link = {
            'slug': 'chainlink',
            'convert': 'USD'
        }

        #Access Key CoinMarketCap API
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '7b3r6u13-e0ap-3400-816f-ba9a0a4af7b4' #Insert the key obtained from your CoinMarketCap account.
        }

        session = Session()
        session.headers.update(headers)

        #Personal details (Tweepy)
        consumer_key = 'e5li8B6cfykjNEeyqxX4GNwzn' #Insert the key obtained from your Twitter account.
        consumer_secret = 'Flum69PWJQjk7cI7SiYfRlT6JT3tAo0MQRBVT83LSgc7Tjo2BA' #Insert the key obtained from your Twitter account.
        access_token = '1395928461425710088-v7XvUYOpYwjASuzAVa9cIphHQiZBKd' #Insert the key obtained from your Twitter account.
        access_token_secret = 'WBBdXonBp20MhZXulp5JZvx7CWA9pdVf7LJwXHTdTDs01' #Insert the key obtained from your Twitter account.

        #Authenticate to Twitter (Tweepy)
        authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_token_secret)

        #Create API object (Tweepy)
        api = tweepy.API(authentication, wait_on_rate_limit = True)

        #From here on down, the quotes are captured and the tweet is created.
 
        #bitcoin
        response = session.get(url, params = parameters_btc)
        price_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['price'])
        change_24h_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['percent_change_24h'])

        #ethereum
        response = session.get(url, params = parameters_eth)
        price_eth = float(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
        change_24h_eth = float(json.loads(response.text)['data']['1027']['quote']['USD']['percent_change_24h'])

        #binance coin
        response = session.get(url, params = parameters_bnb)
        price_bnb = float(json.loads(response.text)['data']['1839']['quote']['USD']['price'])
        change_24h_bnb = float(json.loads(response.text)['data']['1839']['quote']['USD']['percent_change_24h'])

        #cardano
        response = session.get(url, params = parameters_ada)
        price_ada = float(json.loads(response.text)['data']['2010']['quote']['USD']['price'])
        change_24h_ada = float(json.loads(response.text)['data']['2010']['quote']['USD']['percent_change_24h'])

        #ripple
        response = session.get(url, params = parameters_xpr)
        price_xrp = float(json.loads(response.text)['data']['52']['quote']['USD']['price'])
        change_24h_xrp = float(json.loads(response.text)['data']['52']['quote']['USD']['percent_change_24h'])

        #doge coin
        response = session.get(url, params = parameters_doge)
        price_doge = float(json.loads(response.text)['data']['74']['quote']['USD']['price'])
        change_24h_doge = float(json.loads(response.text)['data']['74']['quote']['USD']['percent_change_24h'])

        #internet computer
        response = session.get(url, params = parameters_icp)
        price_icp = float(json.loads(response.text)['data']['8916']['quote']['USD']['price'])
        change_24h_icp = float(json.loads(response.text)['data']['8916']['quote']['USD']['percent_change_24h'])

        #chainlink
        response = session.get(url, params = parameters_link)
        price_link = float(json.loads(response.text)['data']['1975']['quote']['USD']['price'])
        change_24h_link = float(json.loads(response.text)['data']['1975']['quote']['USD']['percent_change_24h'])

        time.gmtime() #Taking the UTC time zone to apply it to the tweet.
        from time import gmtime, strftime
        hour = strftime("%a, %d %b %Y %H:%M:%S UTC", gmtime())

        api.update_status('BTC: ${:.2f}'.format(price_btc) + ' ↔️ % 24h: {:.2f}'.format(change_24h_btc) + '\n'+
                          'ETH: ${:.2f}'.format(price_eth) + ' ↔️ % 24h: {:.2f}'.format(change_24h_eth) + '\n'+
                          'BNB: ${:.2f}'.format(price_bnb) + ' ↔️ % 24h: {:.2f}'.format(change_24h_bnb) + '\n'+
                          'ADA: ${:.2f}'.format(price_ada) + ' ↔️ % 24h: {:.2f}'.format(change_24h_ada) + '\n'+
                          'XRP: ${:.2f}'.format(price_xrp) + ' ↔️ % 24h: {:.2f}'.format(change_24h_xrp) + '\n'+
                          'DOGE: ${:.2f}'.format(price_doge) + ' ↔️ % 24h: {:.2f}'.format(change_24h_doge) + '\n'+
                          'ICP: ${:.2f}'.format(price_icp) + ' ↔️ % 24h: {:.2f}'.format(change_24h_icp) + '\n'+
                          'LINK: ${:.2f}'.format(price_link) + ' ↔️ % 24h: {:.2f}'.format(change_24h_link) + '\n'+
			              '\n🕑 ' + hour)
        
        print('Successfully tweeted.', hour)
        time.sleep(900)#15 in 15 minutes. 

    except tweepy.TwitterServerError as e:
        print('\nError:', e.reason, '\n')

    except StopIteration:
        break
