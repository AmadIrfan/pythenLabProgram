import Funcs as f 

Arr=[3,4,7,-1,0,1,23,-2,-5]

start=input('Enter Starting index : ')
starting=int(start)
end=input('Enter Ending index : ')
ending=int(end)

integer=f.Minimum(Arr,starting,ending +1) 
print(integer)