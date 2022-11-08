from funcs import SearchA
file=open('text.txt',mode='r')
line=file.read()
arr1=line.split(',')

Arr=[]
for a in arr1:
    Arr.append(a)
    

x=input('Enter the Number you want to Search : ')
array=SearchA(Arr, x)
ind=0
for i in array:
    if(ind!=0):
        print(end=',')
    print(i,end=' ')
    ind+=1