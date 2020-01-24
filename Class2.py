# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:39:46 2020

@author: DELL
"""

class employee:
    empCount= 0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount+=1
        def displayCount(self):
            print("Total emplo %d" % employee.empCount)
    def displayEmployee (self):
        print ("Name: " ,self.name, ",Salary:",self.salary)