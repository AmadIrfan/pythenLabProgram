import time
from funcs import RandomArray
from funcs import InsertionSort
#Generate Random numbers
arr = RandomArray(100) 

#Take starting and ending index to apply insertion sort
start = int(input("Enter starting index "))
end = int(input("Enter ending index "))

#save starting time
start_time = time.time() 

#Call Insertion sort function
Arr = InsertionSort(arr, start, end)

#save ending time
end_time = time.time() 

#to write the sorted portion of array in text file
s = (Arr[start:end:1]) 
file = open("SortedInsertionSort.csv",mode = "w")
for i in s:
    file.write(str(i)+"\n")

# print the sorted array
print(Arr) 

# calculate run time of insertion function
run_time = end_time - start_time 

#print run time of function
print("Runtime of insertion sort in seconds is  ",run_time,"seconds")
