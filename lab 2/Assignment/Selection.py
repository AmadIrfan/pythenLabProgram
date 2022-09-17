import time
import funcs as f


start = int(input("Enter starting index "))
end = int(input("Enter ending index "))


arr=f.RandomArray(30000)
startTime=time.time()

#Time Starts for requird to calculate required time
startTime=time.time()
#function that returns partialy sorrted array
arr1=f.SelectionSort(arr,start,end)                
#Time end After calculate time
endTime=time.time()
#total time
totalTime=endTime-startTime

print(arr1)

file=open('SortedBubbleSort.csv',mode='w')
for i in arr1:
    file.write(str(i) + '\n')

print( 'Time Taken',totalTime)