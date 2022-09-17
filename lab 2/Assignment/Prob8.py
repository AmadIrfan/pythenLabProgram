
import time as tm
import funcs as f
import random

#array
array=[1,2,3,4,5,6,7,8,9,10]
#reading data from file

file=open("words.txt",'r')
lines=file.read()
arr=lines.split('\n')


def ShuffleArray(Array,start,end):
   
    return Array

sTime=tm.time()
err=f.InsertionSort(array,0,len(array))
eTime=tm.time()
tTime=eTime-sTime
print(tTime)
print(array) 


sArr=ShuffleArray(array,0,len(array))
print(sArr)