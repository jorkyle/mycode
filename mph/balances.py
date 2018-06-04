#!/usr/bin/env python3

#Written by: Kyle Jorgensen

#This script pulls a user's balances from Mining Pool Hub and prints the data
#in a readable format.  Thanks to RoryHolland for most of the list of symbols.
#Plan to add functionality for other API calls from Mining Pool Hub using this
#same framework.

##Import the following for web request, json, and pretty printing
import requests
import json
import pprint
import getpass

##List of current currencies supported by Mining Pool Hub
symbols = {
  "adzcoin": "ADZ",
  "auroracoin": "AUR",
  "bitcoin": "BTC",
  "bitcoin-cash": "BCH",
  "bitcoin-gold": "BTG",
  "bitcoin-private": "BTCP",
  "dash": "DSH",
  "digibyte": "DGB",
  "digibyte-groestl": "DGB",
  "digibyte-skein": "DGB",
  "digibyte-qubit": "DGB",
  "electroneum": "ETN",
  "ethereum": "ETH",
  "ethereum-classic": "ETC",
  "expanse": "EXP",
  "feathercoin": "FTC",
  "gamecredits": "GAME",
  "geocoin": "GEO",
  "globalboosty": "BSTY",
  "groestlcoin": "GRS",
  "litecoin": "LTC",
  "maxcoin": "MAX",
  "monacoin": "MONA",
  "monero": "XMR",
  "musicoin": "MUSIC",
  "myriadcoin": "XMY",
  "myriadcoin-skein": "XMY",
  "myriadcoin-groestl": "XMY",
  "myriadcoin-yescrypt": "XMY",
  "sexcoin": "SXC",
  "siacoin": "SC",
  "startcoin": "START",
  "verge": "XVG",
  "vertcoin": "VTC",
  "zcash": "ZEC",
  "zclassic": "ZCL",
  "zcoin": "XZC",
  "zencash": "ZEN"
}

##Set variables for the base URL for MPH, API call, and prompt the user for
##their API key.  I kept the url, api_method, and balance command separate
##for modularity in expanding functions.
url = 'https://miningpoolhub.com/index.php?'
api_method = 'page=api&action='
balance = 'getuserallbalances'
mykey = '&api_key=' + getpass.getpass('Input your API Key: ')

##This block combines the specific API function and loads the JSON.
balance_url = url + api_method + balance + mykey
balance_page = requests.get(balance_url).text
balance_json = json.loads(balance_page)

##This block creates a total balance for each individual coin in the nested
##dictionary returned by the previous block and returns the key/value pairs
##from the subkeys.
coins = {}
for coin in balance_json["getuserallbalances"]["data"]:
    symbol = symbols[coin["coin"]]
    balance = sum([
      coin["confirmed"],
      coin["unconfirmed"],
      coin["ae_confirmed"],
      coin["ae_unconfirmed"],
      coin["exchange"]
     ])
    coins[symbol] = balance
pprint.pprint(coins) #Pretty print the results
