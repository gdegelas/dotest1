import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

def peak_detect(price,order=3):

    max_idx = list(argrelextrema(price, np.greater,order=order)[0])
    min_idx = list(argrelextrema(price, np.less,order=order)[0])
    
    print()
    idx = max_idx + min_idx + [len(price)-1]

    idx.sort()
    
    current_idx = idx[-5:]
    
    start = min(current_idx)
    end = max(current_idx)
    
    current_pat = price[current_idx]
    print(current_pat)
    return current_idx,current_pat,start,end

def is_gartley(moves,error_allowed):
    
    XA = moves[0]
    AB = moves[1]
    BC = moves[2]
    CD = moves[3]
    DE = moves[4]
    
    AB_range = np.array([0.618 - error_allowed, 0.618 + error_allowed])*abs(XA)
    BC_range = np.array([0.382 - error_allowed, 0.886 + error_allowed])*abs(AB)
    CD_range = np.array([1.272 - error_allowed, 1.618 + error_allowed])*abs(BC)
    DE_range = np.array([0.10 - error_allowed, 0.10 + error_allowed])*abs(CD)])
    
    if XA>0 and AB<0 and BC>0 and CD<0:
         
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return 1
        
        else:
            
            return np.NAN

    if XA<0 and AB>0 and BC<0 and CD>0:
        
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return -1
        
        else:
            
            return np.NAN
        
    return np.NAN

def is_butterfly(moves,error_allowed):
    
    XA = moves[0]
    AB = moves[1]
    BC = moves[2]
    CD = moves[3]
    
    AB_range = np.array([0.786 - error_allowed, 0.786 + error_allowed])*abs(XA)
    BC_range = np.array([0.382 - error_allowed, 0.886 + error_allowed])*abs(AB)
    CD_range = np.array([1.618 - error_allowed, 2.618 + error_allowed])*abs(BC)

    if XA>0 and AB<0 and BC>0 and CD<0:
         
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return 1
        
        else:
            
            return np.NAN

    if XA<0 and AB>0 and BC<0 and CD>0:
        
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return -1
        
        else:
            
            return np.NAN
        
    return np.NAN

def is_crab(moves,error_allowed):
    
    XA = moves[0]
    AB = moves[1]
    BC = moves[2]
    CD = moves[3]
    
    AB_range = np.array([0.382 - error_allowed, 0.618 + error_allowed])*abs(XA)
    BC_range = np.array([0.382 - error_allowed, 0.886 + error_allowed])*abs(AB)
    CD_range = np.array([2.618 - error_allowed, 3.618 + error_allowed])*abs(BC)

    if XA>0 and AB<0 and BC>0 and CD<0:
         
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return 1
        
        else:
            
            return np.NAN

    if XA<0 and AB>0 and BC<0 and CD>0:
        
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return -1
        
        else:
            
            return np.NAN
        
    return np.NAN

def is_bat(moves,error_allowed):
    
    XA = moves[0]
    AB = moves[1]
    BC = moves[2]
    CD = moves[3]
    
    AB_range = np.array([0.382 - error_allowed, 0.5 + error_allowed])*abs(XA)
    BC_range = np.array([0.382 - error_allowed, 0.886 + error_allowed])*abs(AB)
    CD_range = np.array([1.618 - error_allowed, 2.618 + error_allowed])*abs(BC)

    if XA>0 and AB<0 and BC>0 and CD<0:
         
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return 1
        
        else:
            
            return np.NAN

    if XA<0 and AB>0 and BC<0 and CD>0:
        
        if AB_range[0] < abs(AB) < AB_range[1] and BC_range[0] < abs(BC) < BC_range[1] and CD_range[0] < abs(CD) < CD_range[1]:
            
            return -1
        
        else:
            
            return np.NAN
        
    return np.NAN
