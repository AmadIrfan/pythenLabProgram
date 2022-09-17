


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
    index=0
    ending=ending+1
    minim=0
    for i in range(starting,ending):
        if Arr[i] <= minim:
            minim=Arr[i]
            index=i
    integer=index        
    return integer


def StringReverse(str, starting,ending):
    newLine=str[starting: ending]
    string=newLine[::-1]
    return string
    
def RowWiseSum(Met):
    rowSum=[]
    for i in range(0,len(Met)):
        sum=0
        for j in range(3):
            sum=Met[i][j]+sum
        rowSum.append(sum)
    return rowSum


def Sort4(Arr):
    lengthArr=len(Arr)
    array=[]
    while lengthArr > 0 :
        minimum=Arr[0]
        for i in Arr:
            if (i < minimum):
                minimum=i
        array.append(minimum)
        Arr.remove(minimum)
        lengthArr=len(Arr)
    return array

def ColumnWiseSum(Met):
    colSum=[]
    for i in range(0,len(Met)):
        sum=0
        for j in range(3):
            sum=Met[j][i]+sum
        colSum.append(sum)
    return colSum

def PalindromRecursive(str):
 
    lengthStr=len(str)
    S=str[0]
    E=str[-1]
    if(lengthStr<=1):
        return True
    else :
        if(S==E):
            word=str[1:-1]
            return PalindromRecursive(word)
        else :
            return False; 



def SortedMerge(Arr1,Arr2):    
    array1=[]
    array=[]
    array1=Arr1+Arr2
    for i in range(len(array1)):
        minimum=array1[0]
        for x in array1:
            if(x<minimum):
                minimum=x
        array.append(minimum)
        array1.remove(minimum)
    return array

def SumIterative(number):
    integer=0
    while number != 0:
        num=number%10
        integer=integer+num
        number=number//10
    return integer

def Sort10(Arr):
    array=[]
    nArr=[]
    pArr=[]
    index=0
    const=0
    for i in Arr:
        if i < const:
            nArr.append(i)
        if i>=const:
            pArr.append(i)
    nArr.sort()
    pArr.sort()
    
    for i in pArr:
        array.append(i)
    for j in nArr:
        array.insert(index,j)
        index += 2
    return array


def SumRecursive(number):
    integer=0
    if number==0:
        integer=0
        return integer
    
    else:
        return SumRecursive(number//10) + number%10