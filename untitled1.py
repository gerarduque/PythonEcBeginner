# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:04:32 2020

@author: DELL
"""

import math

x=float(input("Enter x:"))
y=math.sqrt(x)

print("The sqrt root of ",x,"equals to ",y)


try:
    print("1")
    x=1/0
    print("2")
except:
    print("smt wrong")
print("3")


try:
    x=int(input("number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("can not divide by zero")
except ValueError:
    print("must enter an integer value")
except:
    print("somth worng")
print("End")