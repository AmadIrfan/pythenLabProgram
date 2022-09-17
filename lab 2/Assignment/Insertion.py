import time
import funcs as f

array=f.RandomArray(30000)

start=input('Enter Starting index ')
end=input('Enter ending index ')


startTime=time.time()
arr=f.InsertionSort(array, start, end)
endTime=time.time()
totalTime=endTime-startTime


file=open('SortedInsertionSort.csv',mode='w')
for i in arr:
    file.write(str(i) + '\n')

print( 'Time Taken',totalTime)


