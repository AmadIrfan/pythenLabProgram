import random
import math

def RandomArray(size):
    arr = []
    for i in range(size):
        num = random.randint(0,size)
        arr.append(num)
    return arr

def InsertionSort(array,start,end):
    for j in range(start,end):
        key = array[j]
        i = j-1
        while(i>=0 and array[i] > key):
            array[i+1] = array[i]
            i=i-1
            array[i+1] = key
            
    return array

def BubbleSort(array,start,end):
    j = len(array)
    sorted = False
    while((j > 1) and (not(sorted))):
        sorted = True
        for i in range(start,end):
            if(array[i-1] > array[i]):
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
                sorted = False
    return array
 
def SelectionSort(array,start,end):
    for i in range(end):
        min = i
        for j in range(i + 1, end):
            if array[j] < array[min]:
                min = j         
        array[i], array[min] = array[min], array[i]
        
    return array
    
def ShuffleArray(array,start,end): 
        c = array[start:end:1]      
        random.shuffle(c)
        array[start:end:1] = c
        return array

def Merge(array,p,q,r):
    Left = []
    Right = []
    n1 = q-p+1
    n2 = r-q
    for i in range(n1+1):
        Left.append(array[p+i-1])
    for j in range(n2+1):
        Right.append(array[q+j])
    Left.append(10000000)
    Right.append(10000000) 
    i = 1
    j= 1
    for k in range(p,r+1):
        if(Left[i] <= Right[j]):
            array[k] = Left[i]
            i = i+1
        else:
            array[k] = Right[j]
            j= j+1
            
def MergeSort(array,p,r):
    if(p<r):
        q = math.floor((p+r)/2)
        MergeSort(array,p,q)
        MergeSort(array,q+1,r)
        Merge(array, p, q, r)
    
def HybridMergeSort(array,start,end):
    if(start<end):
        q = math.floor((start+end)/2)
        MergeSort(array,start,end)
        MergeSort(array,q+1,end)
        Merge(array, start, q, end)
    else:
        for j in range(start,end):
            key = array[j]
            i = j-1
            while(i>=0 and array[i] > key):
                array[i+1] = array[i]
                i=i-1
                array[i+1] = key
                
           