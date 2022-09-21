import time
import funcs as f

array=f.RandomArray(100000)

start=input('Enter Starting index ')
end=input('Enter ending index ')

startTime=time.time()
arr=f.InsertionSort(array, int(start), int(end))
endTime=time.time()
totalTime=endTime-startTime


file=open('SortedInsertionSort.csv',mode='w')
for i in arr:
    file.write(str(i) + '\n')

print( 'Time Taken',totalTime)


