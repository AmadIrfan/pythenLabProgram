from json import load
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuickWidgets import * 


A=[]

class heap():
    heapSize=0
    def __init__(self,heapsize):
        self.heapSize=heapsize
        


def left(i):
    return 2*i
def right(i):
    return 2*i+1


def MaxHeapify(A,i):
    l=left(i)
    r=right(i)
    if l<A.heapSize and A[l]<=A[r]:
        largest=l
    else:
        largest=i
    if r<A.heapSize and A[r]<=A[largest]:
        largest=r
    if r != i:
        largest=i
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        MaxHeapify(A,largest)




def Build_Max_Heap(A):
    A.heapSize=A.length
    for i in reversed(range(2,int(len(A)/2))):
        MaxHeapify(A,i)





