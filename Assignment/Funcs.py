


def SearchA(Arr,x):
    indexArray=[]
    print("index : ",end=' ')
    index=0
    for item in Arr:
        if (item==x):
           indexArray.append(index)
        index+=1
    return indexArray


def SearchB():
    print()

def Minimum(Arr,starting,ending):
    ending=ending+1
    minim=0
    for i in range(starting,ending):
        if Arr[i]<=minim:
            minim=Arr[i]
    integer=minim        
    return integer

def StringReverse(str, starting,ending):
    newLine=str[starting: ending]
    string=newLine[::-1]
    return string
    