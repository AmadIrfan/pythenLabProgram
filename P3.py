from random import *
import math
array=[]
def randomArr():
    for i in range(0,20):
        arrValues=randint(0,20)
        array.append(arrValues)

        
def h1(x):
    return x % 7

def h2(x):
    return x % 3
