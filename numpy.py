# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:35:11 2020

@author: DELL
"""

import numpy as np

a= np.array([1,2,3])
print(a)

b=np.array([(1,2,3),(4,5,6)])
print(b)


import numpy as np
import sys
print("uso de memoria python")
S=range(10000)
print(sys.getsizeof(5)*len(S))
print("\n"*1)
print("uso de memoria Numpy")
D=np.arange(10000)
print(D.size*D.itemsize)