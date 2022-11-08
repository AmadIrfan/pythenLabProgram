import time
from funcs import RandomArray
from funcs import MergeSort
#Generate Random numbers
arr = RandomArray(1000000)
#Take starting and ending index to apply merge sort
start = 0
# int(input("Enter starting index "))
end = len(arr)-1
# int(input("Enter ending index "))
s = time.time()
MergeSort(arr,start,end)
e = time.time()
#print(arr[start:end:1])
run = e - s
print("Runtime of merge sort in seconds is: ",run)

#to write the sorted portion of array in text file
s = (arr[start:end:1]) 
file = open("SortedMergeSort.csv",mode = "w")
for i in s:
    file.write(str(i)+"\n")