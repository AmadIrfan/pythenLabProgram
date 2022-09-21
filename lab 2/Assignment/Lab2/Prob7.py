import time
from funcs import RandomArray
from funcs import HybridMergeSort
from funcs import SelectionSort
from funcs import InsertionSort
from funcs import BubbleSort
from funcs import MergeSort
given_file = open(file = 'Nvalues.txt',mode = 'r')

lines = given_file.read()
Arr =[]
arr = lines.split('\n')
for s in arr:
    num = int(s)
    Arr.append(num)
insertionArray = []
bubbleArray = []
mergeArray = []
hybridArray = []
selectionArray = []
start = int(input("Enter starting index "))
end = int(input("Enter ending index "))
for i in Arr:
    arr = RandomArray(i)
    startInsert = time.time() #starting time
    InsertionSort(arr, start, end)
    endInsert = time.time() # ending time
    startbubble = time.time() #starting time
    BubbleSort(arr, start, end)
    endbubble = time.time() # ending time
    startmerge = time.time() #starting time
    MergeSort(arr, start, end)
    endmerge = time.time() # ending time
    starthybrid = time.time() #starting time
    HybridMergeSort(arr, start, end)
    endhybrid = time.time() # ending time
    startselection = time.time() #starting time
    SelectionSort(arr, start, end)
    endselection = time.time() # ending time
    runinsertion = endInsert - startInsert 
    runbubble = endbubble - startbubble
    runmerge = endmerge - startmerge
    runhybrid = endhybrid - starthybrid
    runselection = endselection - startselection
    mergeArray.append(runmerge)
    bubbleArray.append(runbubble)
    hybridArray.append(runhybrid)
    selectionArray.append(runselection)
    insertionArray.append(runinsertion)
    
print(mergeArray)
print(bubbleArray)
print(hybridArray)
print(selectionArray)
print(selectionArray)
file = open("RunTime.csv",mode = "w")
for i in range(0,len(mergeArray)):
    file.write('{0},{1},{2},{3},{4},\n'.format(mergeArray[i],bubbleArray[i],hybridArray[i],selectionArray[i],insertionArray[i]))
    
