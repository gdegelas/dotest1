import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from TradingBot_Patroon import *

# Import our historical data

data = pd.read_csv('DATA/EURUSD.csv')

data.colums = [['Date','Open','High','Low','Close','Volume']]

#data = data.drop_duplicates(keep=False)#

#data.Data = pd.to_datetime(data.Date,format='%d.%m.%Y %H:%M:%S.%f')

#data = data.set_index(data.Date)

data = data.drop_duplicates(keep=False)

data = data[['Open','High','Low','Close','Volume', 'Take Profit']]

price = data.Close.copy()

# Find Peaks

# Toevoegen error

error_allowed = 3.0/100

# Enable to PIPS-array
#pips = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,])

#plt.ion()

for i in range(100,len(price)):

    current_idx,current_pat,start,end = peak_detect(price.values[:i], order=10)
    
    #print("It Works")

    XA = current_pat[1] - current_pat[0]
    #print(XA)
    AB = current_pat[2] - current_pat[1]
    #print(AB)
    BC = current_pat[3] - current_pat[2]
    #print(BC)
    CD = current_pat[4] - current_pat[3]
    #print(CD)
    DE = current_pat[5] - current_pat[4]
    
    moves = [XA,AB,BC,CD,DE]
    
# Patroon
    
    gartley = is_gartley(moves, error_allowed)
    
    butterfly = is_butterfly(moves, error_allowed)
    
    crab = is_crab(moves, error_allowed)
    
    bat = is_bat(moves, error_allowed)

    harmonics = np.array([gartley, butterfly, crab, bat])
    
    labels = ['Gartley','Butterfly','Crab','Bat']
    
    if np.any(harmonics == 1) or np.any(harmonics == -1):
        
        for j in range(0,len(harmonics)):
            
            sense = 'Bearish ' if harmonics[j] == -1 else 'Bullish '
            label = sense + labels[j] + ' Found'
            
            if harmonics[j] == 1:
                 
                # Enable to calculate PIPS 
                #pips += 1000*(price[end+1:end+16] - price[end])
                             
                
                plt.title(label)
                plt.plot(np.arange(start, i+25), price.values[start:i+25])
                plt.plot(current_idx,current_pat,c='r')
                plt.show()
                 
            
            elif harmonics[j] == -1:              
                
                # Enable to calculate PIPS
                #pips += 1000*(price[end:] - price[end+1:end+16])
                
                plt.title(label)
                plt.plot(np.arange(start, i+25), price.values[start:i+25])
                plt.plot(current_idx,current_pat,c='g')
                plt.show()
                print(current_idx)
            
            # Plot Bar Chart - winst PIPS
            #plt.clf()
            #plt.bar(np.arange(1,16),pips)
            #plt.pause(0.05)
            