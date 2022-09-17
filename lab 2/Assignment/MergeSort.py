import funcs as f
import time

start = int(input("Enter starting index "))
end = int(input("Enter ending index "))

array=f.RandomArray(30000)


sTime=time.time()
f.MergeSort(array,int(start),int(end))
eTime=time.time()
print(array)

tTime=eTime-sTime
file=open('SortedMergeSort.csv',mode='w')
for i in array:
    file.write(str(i) + '\n')

print( 'Time Taken',tTime)
