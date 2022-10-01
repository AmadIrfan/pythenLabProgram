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
            if(total > 9 and j > 0 ):
                inner=str(total % 10)+inner
                carry=total//10  
            else:
                inner=str(total)+inner
                carry=0  
        res*=10
        res+=int(inner)
        count+=1
    return res

num1 = int(input("Enter 1st number of integer "))
num2 = int(input("Enter 2nd number of integer "))

result=Multiply_integer(num1,num2)
print("Multiply_integer",result)


def Multiply_Recursive(a, b):
    if ( a<b) :
        return Multiply_Recursive(a, b)
    elif b != 0:
        return a + Multiply_Recursive(a, b-1) 
    else :
        return 0

print('Multiply_Recursive',Multiply_Recursive(num1,num2))


def Karatsuba_Recursive(a, b):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a*b
    else:
        m = max(len(str(a)),len(str(b)))
        m2 = m / 2
        a1 = a / 10**(m2)
        b1 = a % 10**(m2)
        c = b / 10**(m2)
        d = b % 10**(m2)
        abc = Karatsuba_Recursive(b1,d)
        cdf = Karatsuba_Recursive((a1+b1),(c+d))
        efg = Karatsuba_Recursive(a1,c)
        return (efg * 10**(2*m2)) + ((cdf - efg - abc) * 10**(m2)) + (abc)

print("Karatsuba_Recursive",Karatsuba_Recursive(10, 12))    
    



def Multiply_string(a,b):
    arrA=[]
    arrB=[]
    result=0
    count=0
    print('------')
    for i in a:
        arrA.append(int(i))
    for j in b:
        arrB.append(int(j))
    for i in range(len(a)):
        carry=0
        inner=''
        for j in reversed(range(len(b))):
            total=int(a[i])*int(a[j])+carry
            if(total > 9 and j > 0 ):
                inner=str(total % 10)+inner
                carry=total//10  
            else:
                inner=str(total)+inner
                carry=0  
        result*=10
        result+=int(inner)
        count+=1
    return result

y= input("Enter 1nd number of integer as string ")
z= input("Enter 2nd number of integer as string ")

print(Multiply_string(y,z))

def Multiply2(x,y):
    index=0
    last=0
    index2=0
    num=0
    tremin=''
    num2=0
    binary=[]
    arr1=[]
    arr2=[]
    for i in x:
        if(int(i) > 1 or int(i) < 0):
            print("you enterd invalid binary digit 1 ")
            return 0
        else:
            arr1.append(i)
    arr1.reverse()
    for y in y:
        if(int(y) > 1 or int(y) < 0):
            print("you enterd invalid binary digit 2 ")
            return 0
        else:
            arr2.append(y)
    arr2.reverse()
    for x in arr1:
        num=int(x)*pow(2,index)+num  
        index+=1
    for y in arr2:
        num2=int(y)*pow(2,index2)+num2
        index2+=1
    total=num*num2
    while total!=0:
        last=str(total)
        tremin=str(total%2)
        total=total//2
        lastIndex=len(tremin)-1
        for t in range(0,len(tremin)):
            binary.append(int(tremin[t])) 
    binary[lastIndex]=int(last)
    binary.reverse()
    return binary



def Multiply16(x,y):
    index=0
    num=0
    num1=0
    index1=0
    Haxa=[]
    arr1=[]
    arr2=[]
    for ix in x:
        arr1.append(ix)
    arr1.reverse()
    for iy in y:
        arr2.append(iy)
    arr2.reverse()
    for i in arr1:
        if(i=="A"):
            num=10*pow(16,index)+num
            index+=1
        elif(i=="B"):
            num=11*pow(16,index)+num
            index+=1
        elif(i=="C"):
            num=12*pow(16,index)+num
            index+=1
        elif(i=="D"):
            num=13*pow(16,index)+num
            index+=1
        elif(i=="E"):
            num=14*pow(16,index)+num
            index+=1
        elif(i=="F"):
            num=15*pow(16,index)+num
            index+=1
        else:
            num=int(i)*pow(16,index)+num
            index+=1
    for j in arr2:
        if(j=="A"):
            num1=10*pow(16,index1)+num1
            index1+=1
        elif(j=="B"):
            num1=11*pow(16,index1)+num1
            index1+=1
        elif(j=="C"):
            num1=12*pow(16,index1)+num1
            index1+=1
        elif(j=="D"):
            num1=13*pow(16,index1)+num1
            index1+=1
        elif(j=="E"):
            num1=14*pow(16,index1)+num1
            index1+=1
        elif(j=="F"):
            num1=15*pow(16,index1)+num1
            index1+=1
        else:
            num1=int(j)*pow(16,index1)+num1
            index1+=1
    total=Karatsuba_Recursive(num, num)
    inde=0
    while total !=0:
        tremin=str(total%16)
        if(int(tremin)==10):
            tremin="A"    
            Haxa.insert(inde, tremin)
            inde+=1
        elif(int(tremin)==11):
            tremin="B"
            Haxa.insert(inde, tremin)
            inde+=1
        elif(int(tremin)==12):
            tremin="C"
            Haxa.insert(inde, tremin)
            inde+=1
        elif(int(tremin)==13):
            tremin="D"
            Haxa.insert(inde, tremin)
            inde+=1
        elif(int(tremin)==14):
            tremin="E"
            Haxa.insert(inde, tremin)
            inde+=1
        elif(int(tremin)==15):
            tremin="F"
            Haxa.insert(inde, tremin)
            inde+=1
        else:
            Haxa.insert(inde, tremin)
            inde+=1
        total=total//16
    Haxa.reverse()
    return Haxa 
        
arr16=Multiply16("A1","B2")
array=Multiply2("111",'111')       
print('it take to much time for binary and Haxa code')
print(array)
print(arr16)

