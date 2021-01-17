import os
import time
from binance.client import Client
def get_timestamp(): return int(time.time() * 1000)

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

def asset_info():
    global pair
    global quantity
    global leverage
    global threshold
    global stoplimit
    global callbackRate
    global round_decimal
    
    while True:
        print("Here are the supported Coins: ")
        print("1. BTC\n" + "2. ETH\n" + "3. LINK\n" + "4. SUSHI\n")
        input_num = input("Choose your Coin :   ") or '1'

        if input_num == '1': 
            coin            = "BTC"
            quantity        = 0.001
            leverage        = 125
            threshold       = 0.15
            stoplimit       = 0.15
            callbackRate    = 0.3
            round_decimal   = 2
            break

        elif input_num == '2': 
            coin            = "ETH"
            quantity        = 0.01
            leverage        = 100
            threshold       = 0.15
            stoplimit       = 0.15
            callbackRate    = 0.3
            round_decimal   = 2
            break

        elif input_num == '3': 
            coin            = "LINK"
            quantity        = 1
            leverage        = 75
            threshold       = 0.15
            stoplimit       = 0.15
            callbackRate    = 0.3
            round_decimal   = 4
            break

        elif input_num == '4': 
            coin            = "SUSHI"
            quantity        = 1
            leverage        = 50
            threshold       = 0.15
            stoplimit       = 0.15
            callbackRate    = 0.3
            round_decimal   = 4
            break

        else:  print("Invalid Number. Try again.\n")

    pair = coin + "USDT"

    print("Pair Name        :   " + str(pair))
    print("Minimum Quantity :   " + str(quantity))
    print("Maximum Leverage :   " + str(leverage))
    print("Price Movement   :   " + str(threshold))
    print("Stop Limit       :   " + str(stoplimit))
    print("Call Back Rate   :   " + str(callbackRate))
    print("Round Decimal    :   " + str(round_decimal))
    print()

asset_info()

# RealizedPNL
i , overall_PNL = 0, 0 
trades_list = client.futures_account_trades(symbol=pair, timestamp=get_timestamp(), limit=100)
for trade in trades_list:
    overall_PNL = overall_PNL + float(trade.get('realizedPnl'))
    if (float(trade.get('realizedPnl'))) > 0 : 
        i = i + 1
        print(str(i) + ".  " + trade.get('realizedPnl'))
    elif (float(trade.get('realizedPnl'))) < 0 : 
        i = i + 1
        print(str(i) + ". " + trade.get('realizedPnl') + " LOSER TRADE")
    else: continue

print("\n[!] Overall PNL over the last 50 trades: " + str(overall_PNL) + "\n")