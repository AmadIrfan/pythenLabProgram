import time
from funcs import RandomArray
from funcs import HybridMergeSort

#Generate Random numbers
arr = RandomArray(40000)

#Take starting and ending index to apply hybrid sort
start =0
#  int(input("Enter starting index "))
end = len(arr)-1
#  int(input("Enter ending index "))

#calculate starting time
s = time.time()

#call hybrid merge sort function
HybridMergeSort(arr,start,end)

#calculate ending time
e = time.time()

#print(arr[start:end:1]) #only to check the sorted portion
# print(arr)
#calculate run time
run = e - s
print("Runtime of hybrid sort in seconds is: ",run)

#to write the sorted portion of array in text file
s = (arr[start:end:1]) 
file = open("SortedHybridSort.csv",mode = "w")
for i in s:
    file.write(str(i)+"\n")