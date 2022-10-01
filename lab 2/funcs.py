# random imported for generate random numbers
import random

def RandomArray(size):
    array1=[]
    for i in range(0,size):
        randNum=random.randint(0,size)
        array1.append(randNum)
    return array1   

def BubbleSort(array,start,end):
    j=len(array)
    sorted1=False
    while ((j > 1) and (not(sorted1))):
        sorted1=True
        for i in range(start,end):
            if(array[i-1] > array[i]):
                temp=array[i-1]
                array[i-1]=array[i]
                array[i]=temp
                sorted1=False
    return array

def SelectionSort(array ,start,end):
    for i in range(start,end):
        for j in range(0,len(array)-i-1):
            if(array[j]> array[j+1]):
                temp =array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array


def InsertionSort(array,start,end):
    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=0 and key < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

def Merge(Array,p,q,r):
    n1 = q-p+1
    n2 = r-q
    Left = []
    Right = []

    for i in range(n1+1):
        Left.append(Array[p+i-1])
    
    for j in range(n2+1):
        Right.append(Array[q+j])
    
    Left.append(100000000)
    Right.append(100000000) 
    
    i = 1
    j= 1
    
    for k in range(p,r+1):
        if(Left[i] < Right[j]):
            Array[k] = Left[i]
            i = i+1
        else:
            Array[k] = Right[j]
            j= j+1
    return Array


def MergeSort(array,start,end):
    if (start < end):
        q=int((start+end)/2)
        MergeSort(array,start,q)
        MergeSort(array,q+1,end)
        Merge(array,start,q,end)

def HybridMergeSort(array,start,end):
    if (start < end):
        q=int((start+end)/2)
        MergeSort(array,start,q)
        MergeSort(array,q+1,end)
        Merge(array,start,q,end)
    else:
        InsertionSort(array,start,end)