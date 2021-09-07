# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:45:33 2021

@author: HP
"""

# magnitude of a 3D vector
x=1.0
print("x component is",x)
y=2.0
print("y component is",y)
z=3.0
print("z component is",z)
r=pow(x**2+y**2+z**2,0.5)
print("the magnitude of this vector is",r)

# moving right or left 
v=float(input("give me your velocity  :"))
if v>0:
    print("moving right")
elif v<0:
    print("moving left")
else :
    print("not moving")
    
# moving or not moving
from numpy.random import random
force=0.0
ran_fric=random()
mass=10.0
while force<mass*ran_fric :
    print("haha! you cannot move me!!")
    force_add=float(input("add some force!!"))
    force=force+force_add
print("Ah... you win...")
print("the friction coefficient is :",ran_fric)
print("the estimated friction coefficient is :",force/mass)

# calculating factorial
n=int(input("give me an integer, I will give you the factorial"))
factorial=1
for i in range(n):
    factorial=factorial*(i+1)
print("the value of",n,"!","is",factorial)

# eigenvalue problem
import numpy as np
H=np.array([[1,4,6],[4,2,5],[6,5,3]])
w,v=np.linalg.eig(H)
print("the eigenvalues are ",w)
print("the eigenvectors are")
print(v)

# load files
import numpy as np
ex_data=np.loadtxt("external_file.txt")
print(ex_data)

# define a function to calculate factorial
def fac_cal(n):
    result=1
    for i in range(n):
        result=result*(i+1)
    return result
m=5
res=fac_cal(m)
print(m,"!","=",res)
