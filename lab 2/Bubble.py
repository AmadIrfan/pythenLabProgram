import time
import funcs as f

arr=f.RandomArray(100)

se=0
# input('Enter starting Index ')
en=len(arr)
# input('Enter ending Index ')

#Time Starts for requird to calculate required time
startTime=time.time()
#function that returns partialy sorrted array
array=f.BubbleSort(arr,int(se),int(en))
#Time end After calculate time
endTime=time.time()
#total time
totalTime=endTime-startTime

print(array)

file=open('SortedBubbleSort.csv',mode='w')
for i in array:
    file.write(str(i) + '\n')

print( 'Time Taken',totalTime)
