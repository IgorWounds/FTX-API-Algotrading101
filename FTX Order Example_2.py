#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import time, json
from time import sleep
import FTX_Class

c = FTX_Class.FtxClient(api_key="", api_secret="")

while True:
    try:
        btc_old = requests.get('https://ftx.com/api/markets/BTC-PERP').json()
        print(btc_old['result']['ask'])
    except Exception as e:
        print(f'Error obtaining BTC old data: {e}')
    
    sleep(300)
    
    try:
        btc_new = requests.get('https://ftx.com/api/markets/BTC-PERP').json()
        print(btc_new['result']['ask'])
    except Exception as e:
        print(f'Error obtaining BTC new data: {e}')
    
    percent = (((float(btc_new['result']['ask']) - float(btc_old['result']['ask'])) * 100) / float(btc_old['result']['ask']))
    
    if percent < 5:
        print(f'The trade requirement was not satisfied. Percentage move is at {percent}')
        continue
    
    elif btc_data['result']['ask'] >= 5:
        try:
            r = c.place_order("ETH/USD", "buy", 1800.0, 0.006, "1243")
            print(r)
        except Exception as e:
            print(f'Error making order request: {e}')
        
        sleep(2)
        
        try:
            check = c.get_open_orders(r['id'])
        except Exception as e:
            print(f'Error checking for order status: {e}')
            
        if check[0]['status'] == 'open':
            print ('Order placed at {}'.format(pd.Timestamp.now()))
            break
        else:
            print('Order was either filled or canceled at {}'.format(pd.Timestamp.now()))
            break

