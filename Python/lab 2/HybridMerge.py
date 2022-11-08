import funcs as f

import time

start = int(input("Enter starting value :"))
end = int(input("Enter ending value :"))

array=f.RandomArray(30000)

sTime=time.time()
f.HybridMergeSort(array,int(start),int(end))
eTime=time.time()
print(array)

tTime=eTime-sTime
file=open('HybridMergeSort.csv',mode='w')
for i in array:
    file.write(str(i) + '\n')

print( 'Time Taken',tTime)
