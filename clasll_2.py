# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:04:02 2020

@author: DELL
"""
def isYearLeap(year):
   
    
    #print(n)
    #for i in n:
        if year%4 !=0:
            return Fasle
        elif year%100!=0:
            return False
        elif year%400!=0:
            return False
        else:
            return True
         
print(isYearLeap(1900))
