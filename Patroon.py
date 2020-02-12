import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

# Import our historical data

data = pd.read_csv('DATA/BTCUSD.csv')

data.colums = [['Date','Open','High','Low','Close','Volume']]

#data = data.drop_duplicates(keep=False)#

data.Data = pd.to_datetime(data.Date,format='%d.%m.%Y %H:%M:%S.%f')

data = data.set_index(data.Date)

data = data.drop_duplicates(keep=False)

data = data[['Open','High','Low','Close','Volume']]

price = data.Close.iloc[:500]

# Find Peaks

for i in range(100,len(price)):

    max_idx = list(argrelextrema(price.values[:i],np.greater,order=10)[0])
    min_idx = list(argrelextrema(price.values[:i],np.less,order=10)[0])

    idx = max_idx + min_idx + [len(price.values[:i])-1]

    idx.sort()
    
    current_idx = idx[-5:]
    
    start = min(current_idx)
    end = max(current_idx)
    
    current_pat = price.values[current_idx]

    XA = current_pat[1] - current_pat[0]
    AB = current_pat[2] - current_pat[1]
    
    if XA>0 and AB<0:

        plt.plot(np.arange(start,i),price.values[start:i])
        plt.plot(current_idx,current_pat,c='r')
        plt.show()
