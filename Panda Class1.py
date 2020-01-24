# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:24:29 2020

@author: DELL
"""

import numpy as np
import pandas as pd

data = np.array([["","col1","col2"],["fila1",11,22],["fila2",33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))