# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:26:32 2020

@author: DELL
"""

def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end=" ")
        a,b = b,a+b
    print()

#fib()