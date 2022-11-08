import time as tm
import funcs as f
import random


file=open("words.txt",'r')
lines=file.read()
arr=lines.split('\n')
array=[]

#array
#reading data from file
for ij in arr:
    array.append(ij)



def ShuffleArray(Array,start,end):
    for i in range(start,end-1):
        rendom_index=random.randrange(start,end-1)
        temp=Array[i]
        Array[i]=Array[rendom_index]
        Array[rendom_index]=temp
    return Array

oldArray=[]

oldArray=array

sTime=tm.time()
err=f.InsertionSort(array,0,len(array))
eTime=tm.time()
tTime=eTime-sTime
print(tTime)


sArr=ShuffleArray(array,0,len(array))


sTime=tm.time()
err1=f.InsertionSort(sArr,0,len(array))
eTime=tm.time()
tTime=eTime-sTime
print(tTime)


mSTime=tm.time()
err=f.MergeSort(oldArray,0,10)
mETime=tm.time()
mTTime=mETime-mSTime
print(mTTime)
