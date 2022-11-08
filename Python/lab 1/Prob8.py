from funcs import SortedMerge 


A=[]
B=[]
fil=open('data1.txt',mode='r')
line1=fil.read()
arr1=line1.split(',')
for i in arr1:
    A.append(int(i))


fil1=open('data2.txt',mode='r')
line2=fil1.read()
arr2=line2.split(',')
for j in arr2:
    B.append(int(j))


array=SortedMerge(A,B)     
print(array)