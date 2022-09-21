import funcs as f
import time

# start = int(input("Enter starting index "))
# end = int(input("Enter ending index "))

array=f.RandomArray(100)
start=0
end=100

sTime=time.time()
f.MergeSort(array,int(start),int(end))
eTime=time.time()

tTime=eTime-sTime
file=open('SortedMergeSort.csv',mode='w')
for i in array:
    file.write(str(i) + '\n')

print( 'Time Taken',tTime)
