# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:28:44 2019

@author: UPS

TEST DE VELICIDAD
"""
import numpy as np
import time
 
SIZE = 1000000
 
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
print ("\n"*1)
print ("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
print ("\n"*2)
print ("RESULTADO USANDO NUMPY")
start=time.time()
result= A1+A2
print((time.time()-start)*1000)


unos=np.ones((3,4))
print(unos)


ceros=np.zeros((3,4))
print(ceros)



print(np.random.random((3,4)))

print(np.empty((3,4)))


print(np.full((3,4),9))


print(np.arange(0,30,5))

print(np.linspace(0,2,5))



print(np.linspace(0,2,89))


print(np.eye(4,4))



print(np.identity(4))


print((np.array([(1,2,3),(4,5,6)]).dim)


a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)



a=np.array([(1,2,3),(4,5,6)])
print(a.dtype)


a=np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)


a=np.array([(1,2,3),(4,5,6)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)


a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])



a=np.array([(1,2,3,4),
            (3,4,5,6)])

print(a[0:,1])
print(a.min())
print(a.max())
print(a.sum())



a=np.array([(1,2,3),
            (3,4,5)])
print("\n"*2)
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))



a=np.array([(1,2,3),
            (3,4,5)])

y=np.array([(1,2,4),(3,42,6)])

print(a*y)