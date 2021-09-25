#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:34:23 2020

@author: Saad
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime 

apple = yf.Ticker("AAPL")
start_date = '2020-12-01'
end_date = datetime.today().strftime('%Y-%m-%d')
hist_Data = apple.history(interval = "1d" , start = start_date , end = end_date )
data_frame = pd.DataFrame(hist_Data)
date = data_frame.iloc[:,0]
close = data_frame.iloc[:,3]

plt.style.use('seaborn-whitegrid')
plt.subplot(2,1,1)
plt.plot(close, linestyle = 'solid' , color = 'black', label ='Close')

print(date)