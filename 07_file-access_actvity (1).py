# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:03:17 2020

@author: ANGELO
"""

file=open("devices.txt","a")
while True:
    newitem=input("Ingrese nuevas palabras")
    if newitem == "exit":
        break
    file.write(newitem + "\n")
print("All done!")

file.close()