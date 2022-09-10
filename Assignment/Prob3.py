import Funcs as f 

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

integer=f.Minimum(Arr,starting,ending) 
print(integer)