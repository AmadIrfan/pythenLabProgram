from funcs import Minimum 



fil=open('data.txt',mode='r')
lines=fil.read()
Arr=[]
arr1=lines.split(',')
for i in arr1:
    Arr.append(int(i))
start=input('Enter Starting index : ')
starting=int(start)
end=input('Enter Ending index : ')
ending=int(end)

integer=Minimum(Arr,starting,ending) 
print(integer)