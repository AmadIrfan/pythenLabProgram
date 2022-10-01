import time
from funcs import InsertionSort
from funcs import MergeSort
from funcs import ShuffleArray
given_file = open(file = 'words.txt',mode = 'r')

lines = given_file.read()
Arr =[]
arr = lines.split('\n')
for s in arr:
    num = s
    Arr.append(num)
# take starting and ending index
start = int(input("Enter starting index "))
end = int(input("Enter ending index "))

#calculate starting time
start_time = time.time()

#Call Insertion sort function
arr = InsertionSort(Arr, start, end)

#calculate ending time
end_time = time.time()

#calculate run time
run_time = end_time - start_time
print("Runtime of insertion sort in seconds is  ",run_time,"seconds")

#print the shuffle array
shuffleArray = ShuffleArray(Arr, start, end)

shufflestart = time.time()
InsertionSort(shuffleArray,start,end)
shufflend = time.time()
shufflerun = shufflend - shufflestart
print("Runtime of shuffled insertion sort in seconds is  ",shufflerun,"seconds")



'''#calculate starting time
smerge = time.time()

#Call Merge sort function
MergeSort(Arr,start,end)

#calculate ending time
emerge = time.time()

#calculate run time
run = emerge - smerge
print("Runtime of merge sort in seconds is  ",run,"seconds")
'''
