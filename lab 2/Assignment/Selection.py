import time
import funcs as f

arr=f.RandomArray(40000)
#  int(input("Enter starting index "))
# int(input("Enter ending index "))

start =0
end = len(arr)
startTime=time.time()

#Time Starts for requird to calculate required time
startTime=time.time()
#function that returns partialy sorrted array
arr1=f.SelectionSort(arr,start,end)                
#Time end After calculate time
endTime=time.time()
#total time
totalTime=endTime-startTime

# print(arr1)

file=open('SortedBubbleSort.csv',mode='w')
for i in arr1:
    file.write(str(i) + '\n')

print( 'Time Taken',totalTime)