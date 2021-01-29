import binance_futures
from datetime import datetime
from termcolor import colored
from get_hour import get_hour
from get_minute import recent_minute
from get_position import get_position_info

def fomo_trade():
    position_info = get_position_info()
    minute_candle = recent_minute()

    if position_info == "LONGING":
        if (minute_candle == "RED") or (minute_candle == "RED_INDECISIVE"):
            print("ACTION           :   💰 CLOSE_LONG 💰")
            binance_futures.close_position("LONG")
        else: print(colored("ACTION           :   HOLDING_LONG", "green"))

    elif position_info == "SHORTING":
        if (minute_candle == "GREEN") or (minute_candle == "GREEN_INDECISIVE"):
            print("ACTION           :   💰 CLOSE_SHORT 💰")
            binance_futures.close_position("SHORT")
        else: print(colored("ACTION           :   HOLDING_SHORT", "red"))

    else:
        if (minute_candle == "GREEN"):
            print(colored("ACTION           :   🚀 GO_LONG 🚀", "green"))
            binance_futures.open_position("LONG")
        elif (minute_candle == "RED"):
            print(colored("ACTION           :   💥 GO_SHORT 💥", "red"))
            binance_futures.open_position("SHORT")
        else: print("ACTION           :   🐺 WAIT 🐺")

    print("Last action executed @ " + datetime.now().strftime("%H:%M:%S") + "\n")