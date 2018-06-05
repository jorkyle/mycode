#!/usr/bin/env python3

#Written by: Kyle Jorgensen

#This script pulls a user's workers from Mining Pool Hub and prints the data
#in a readable format.  Thanks to RoryHolland for most of the list of symbols.
#Plan to add functionality for other API calls from Mining Pool Hub using this
#same framework.

##Import the following for web request, json, and getpass for API Key
import requests
import json
import getpass

##Dictionary of current currencies supported by Mining Pool Hub. Most are
##currently commented out for personal use (these are the ones I mine) but plan
##to integrate with balances function to automatically choose which currencies
##to poll for worker stats.
symbols = {
#  "adzcoin": "ADZ",
#  "auroracoin": "AUR",
#  "bitcoin": "BTC",
#  "bitcoin-cash": "BCH",
  "bitcoin-gold": "BTG",
  "bitcoin-private": "BTCP",
#  "dash": "DSH",
#  "digibyte": "DGB",
#  "digibyte-groestl": "DGB",
#  "digibyte-skein": "DGB",
#  "digibyte-qubit": "DGB",
  "electroneum": "ETN",
#  "ethereum": "ETH",
#  "ethereum-classic": "ETC",
#  "expanse": "EXP",
#  "feathercoin": "FTC",
#  "gamecredits": "GAME",
#  "geocoin": "GEO",
#  "globalboosty": "BSTY",
#  "groestlcoin": "GRS",
#  "litecoin": "LTC",
#  "maxcoin": "MAX",
#  "monacoin": "MONA",
  "monero": "XMR",
#  "musicoin": "MUSIC",
#  "myriadcoin": "XMY",
#  "myriadcoin-skein": "XMY",
#  "myriadcoin-groestl": "XMY",
#  "myriadcoin-yescrypt": "XMY",
#  "sexcoin": "SXC",
#  "siacoin": "SC",
#  "startcoin": "START",
#  "verge": "XVG",
#  "vertcoin": "VTC",
  "zcash": "ZEC",
  "zclassic": "ZCL",
#  "zcoin": "XZC",
  "zencash": "ZEN"
}

##Set variables for the base URL for MPH, API call, and prompt the user for
##their API key.  Added https_url because each coin name is inserted in the
##address for worker stats.
https_url = 'https://'
url = 'miningpoolhub.com/index.php?'
api_method = 'page=api&action='
workers = 'getuserworkers'
mykey = '&api_key=' + getpass.getpass('Input your API Key: ')

##The following block polls each coin in the symbols dictionary above and
##makes the API call. The sub loop returns only the hashrate of the current
##coin and prints the value if it's more than zero.
for i in list(symbols):
    work_coin = i
    worker_url = https_url + i + '.' + url + api_method + workers + mykey
    workers_page = requests.get(worker_url).text
    workers_json = json.loads(workers_page)
    coin_miners = workers_json['getuserworkers']['data']
    symbol = symbols[i]
    for k in coin_miners:
        if k['hashrate'] > 0:
            print(symbol)
            print(k['hashrate'])
        else:
            pass
