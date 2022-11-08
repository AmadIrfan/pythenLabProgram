

def Multiply_integer(a,b):
    arrA=[]
    arrB=[]
    res=0
    count=0
    print(a)
    print(b)
    print('------')
    ab=str(a)
    cd=str(b)
    for i in ab:
        arrA.append(int(i))
    for j in cd:
        arrB.append(int(j))
    lenArr1=len(arrA)
    lenArr2=len(arrB)
    for i in range(lenArr1):
        carry=0
        inner=''
        for j in reversed(range(lenArr2)):
            total=int(arrA[i])*int(arrB[j])+carry
            print(total,end='')
            if(total > 9 and j > 0 ):
                inner=str(total % 10)+inner
                carry=total//10  
            else:
                inner=str(total)+inner
                carry=0  
        print()
        res*=10
        res+=int(inner)
        count+=1
    return res


num1 = int(input("Enter 1st number of integer "))
num2 = int(input("Enter 2nd number of integer "))
result=Multiply_integer(num1,num2)
print()
 
def Multiply_Recursive(a1, b1):
    if ( a1<b1) :
        return Multiply_Recursive(a1, b1)
    elif b1 != 0:
        return a1 + Multiply_Recursive(a1, b1-1) 
    else :
        return 0

print(Multiply_Recursive(num1,num2))
