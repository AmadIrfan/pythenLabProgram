import pandas as pd
from  random  import *

array=[]
def randomArr():
    for i in range(0,50000):
        arrValues=randint(0,50000)
        array.append(arrValues)

randomArr()
print(array)

def Partition(Arr,p,r):
    x=Arr[r-1]
    # print(x)
    i=p-1
    # print(i)
    for j in range(p,r-1):
        if x <= Arr[j]:
            i=i+1
            # print(i)
            temp=Arr[i]
            Arr[i]=Arr[j]
            Arr[i]=temp
    temper=Arr[i+1]
    Arr[i+1]=Arr[x]
    Arr[x]=temper
    return i+1

def QuickSort(Arr,p,r):
    if p<r:
        q=Partition(Arr,p,r)
        QuickSort(Arr,p,q-1)
        QuickSort(Arr,q+1,r)
        print(Arr)
    return Arr
print(QuickSort(array,1,len(array)))