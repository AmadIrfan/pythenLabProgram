


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

def ColumnWiseSum(Met):
    colSum=[]
    for i in range(0,len(Met)):
        sum=0
        # print(len(Met[0]))
        for j in range(3):
            sum=Met[j][i]+sum
        colSum.append(sum)
    return colSum

def PalindromRecursive(str):
    lengthStr=len(str)
    if(lengthStr<=1):
        return 'Palindrome'
    else :
        if(str[0]==str[-1]):
            return PalindromRecursive(str[1:-1])
        else :
            return 'no Palindrome'; 


def SortedMerge(Arr1,Arr2):    
    array=[]
    array1=[]
    array=Arr1+Arr2
    for i in range(len(array)):
        minimum=array[0]
        for x in array:
            if(x<minimum):
                minimum=x
        array1.append(minimum)
        array.remove(minimum)
    return array1

def SumIterative(number):
    integer=0
    while number != 0:
        num=number%10
        integer=integer+num
        number=number//10
    return integer

def SumRecursive(number):
    integer=0
    if number==1:
        integer=1
        return integer
    else :
        if():
         else:   
    while number != 0:
        num=number%10
        integer=integer+num
        number=number//10
    return integer
