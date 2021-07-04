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
        btc_data = requests.get('https://ftx.com/api/markets/BTC-PERP').json()
        print(btc_data['result']['ask'])
    except Exception as e:
        print(f'Error obtaining BTC old data: {e}')
    
    if btc_data['result']['ask'] < 32000.0:
        print('The trade requirement was not satisfied.')
        sleep(60)
        continue
    
    elif btc_data['result']['ask'] >= 32000.0:
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

