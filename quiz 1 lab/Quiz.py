
#Question Number 3
def FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high):
    left_sum=-1000000
    sum=0
    for i in reversed(range(low,mid)):
        sum+=A[i]
        if sum >left_sum:
            left_sum=sum
            max_left=i
    right_sum=-100000
    sum=0
    for j in range(mid+1,high):
        sum+=A[j]
        if sum >right_sum:
            right_sum=sum
            max_right=i 
    return (max_left,max_right,(left_sum+right_sum))



def FIND_MAXIMUM_SUBARRAY(A,low,high):   
    if high==low:
        return(low,high,A[low])
    else:
        mid=(low+high)//2
        left_low,left_high,left_sum=FIND_MAXIMUM_SUBARRAY(A, low, mid)
        right_low,right_high,right_sum=FIND_MAXIMUM_SUBARRAY(A,mid+1,high)
        cross_low,cross_high,cross_sum=FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high) 
        if left_sum >=right_sum and left_sum >=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >=left_sum and right_sum >=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)


Arr=[-1,-1,-1,-1,-1,]
Arr1=[2,-3,5,8,-12]

print(FIND_MAXIMUM_SUBARRAY(Arr,0,len(Arr)))

#Question Number 2
def StringOccurenceSmall(x):
    index=0
    arr=[]
    for i in x:
        arr.append(i)
    for i in arr:
        if(i=='a'):
            index+=1
    print('a = ',index)   
    index=0
    for i in arr:
        if(i=='b'):
            index+=1
    print('b = ',index)
    index=0
    for i in arr:
        if(i=='c'):
            index+=1
    print('c = ',index)
    index=0
    for i in arr:
        if(i=='d'):
            index+=1
    print('d = ',index)
    index=0
    for i in arr:
        if(i=='g'):
            index+=1
    print('g = ',index)
    
    
StringOccurenceSmall('AabAdBCaSDcgEd')

#Question number 1


def PrintArray(A,startingIndex,EndingIndex):
    if startingIndex==EndingIndex:
        print(A[startingIndex])        
    else:
        last=A[:-1]
        PrintArray(last,startingIndex,EndingIndex)
        
Arr=[4,5,6,7]
PrintArray(Arr,0,len(Arr))
