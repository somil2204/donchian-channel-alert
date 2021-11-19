import pandas as pd

import numpy as np


import get_csv



def get_alerts(tick,period,pr,interval,price_limit):
    tick=str(tick)
    df = get_csv.get_csv1(tick,pr,interval)
    period=period

    array_date = pd.to_datetime(df.index).date
    array_close = np.array(df['Close'])
    array_open = np.array(df['Open'])
    array_high = np.array(df['High'])
    array_low = np.array(df['Low'])
    #array_volume = np.array(df['No. of Trades'])
      
    ave_20_closing = np.average(array_close[-20:])
    print (f'Limit: {price_limit}, 20 Period Ave: {ave_20_closing}')
    if price_limit < ave_20_closing:
        return []                        
                                

# Function to caculate the high band
    def DchannelUpper(i):
        x = float(0.0)
        if(i < period):
            for j in range(i, -1, -1):
                x = max(array_high[j], x)
        else:
            for j in range(i, i-period, -1):
                x = max(array_high[j], x)
        return x

# Function to caculate the low band


    def DchannelLower(i):
        x = float("inf")
        if(i < period):
            for j in range(i, -1, -1):
                x = min(array_low[j], x)
        else:
            for j in range(i, i-period, -1):
                x = min(array_low[j], x)
        return x


# calculating the high band, n = period

    array_upper = []
    for i in range(0, array_high.size):
        array_upper.append(DchannelUpper(i))



# calculating the low band, n = period

    array_lower = []
    for i in range(0, array_low.size):
        array_lower.append(DchannelLower(i))



# calculating the alerts and date

    alert=[]
    alert_date=[]
    for i in range(len(array_close)):
        if array_high[i]>=array_upper[i-1]:
            alert.append(array_close[i])
            alert_date.append(array_date[i])
         
        
    if len(alert_date)>0:

        print([tick,alert_date[-1]])
        return ([tick,str(alert_date[-1])])
    else:
        return []    
