# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:24:38 2020

@author: DELL
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

import math