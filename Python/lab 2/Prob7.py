# contain an error in calling bubblesort

import funcs as f
import time

file=open("Nvalues.txt",mode="r")
lines=file.read()

arr=lines.split('\n')
array=[]
for i in arr:
    array.append(int(i))

start=0
insertionTime,mergeTime,hybridmergeTime,selectionTime,bubbleTime= -1,-1,-1,-1,-1


file1=open('RunTime.csv',mode='w')
file1.write('Value of n , Insertion Sort , Merge Sort , Hybrid Merge , Selectoin Sort , bubble Sort , \n')

for n in array:
    array=f.RandomArray(5)
    oldArray=array
    end=len(array)

    insertionStartTime=time.time()
    f.InsertionSort(array, start, end)
    insertionEndTime=time.time()
    insertionTime=insertionEndTime-insertionStartTime
    array=oldArray
    
    mergeStartTime=time.time()
    f.MergeSort(array, start, end-1)
    mergeEndTime=time.time()
    mergeTime=mergeEndTime-mergeStartTime
    array=oldArray
    
    hybridMergeStartTime=time.time()
    f.HybridMergeSort(array, start, end-1)
    hybridMergeEndTime=time.time()
    hybridmergeTime=hybridMergeEndTime-hybridMergeStartTime
    
    array=oldArray
    
    selectionStartTime=time.time()
    f.SelectionSort(array, start, end)
    selectionEndTime=time.time()
    selectionTime= selectionEndTime - selectionStartTime
    
    array=oldArray
    
    bubbleStartTime=time.time()
    f.BubbleSort(array,0,end)
    bubbleEndTime=time.time()
    bubbleTime=bubbleEndTime-bubbleStartTime
    
    
    file1.write('{0} , {1} , {2} , {3} , {4} , {5} \n'.format(n,insertionTime,mergeTime,hybridmergeTime,selectionTime,bubbleTime))
