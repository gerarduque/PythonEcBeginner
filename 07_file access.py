# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:03:39 2020

@author: -
"""

file=open("devices.txt","r")
while True:
    newItem=input("Ingrese un nuevo dispositivo: ")
    if newItem=="exit":
            break
   
    
    for item in file:
        item=item.strip("a")
     
        
      
        print(item)
        
file.close()




