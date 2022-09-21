
def Multipty(a,b):
    arr=[[],[]]
    arrA=[]
    arrB=[]
    print(a)
    print(b)
    print('------')
    while b % 10 != 0:
        x=b%10
        b=b//10
        arrA.append(x)
        arrA.reverse()
        print(arrA)
    while a % 10 != 0:
        y=a%10
        a=a//10
        arrB.append(y)
        arrB.reverse()
        print(arrB)
        #for i in arrA:
         #   for j in arrB:
          #      print(arr[i][j])



"""
    carry=0
    sum=0  
    while b % 10 != 0:
        x=b % 10
        b=b//10
        arr.append(x)
        while a%10 != 0:
            c=a%10  
            a=a//10
            arr1.append(c)
            A=x*c+carry
            print(A)
            if(A>=10):
                n=A%10
                carry=A//10
                print(carry)
            arr.append(n)
"""



#a=int(input('Enter number 1 :'))

a=4872432141
b=1132312421

#b=int(input('Enter number 2 :'))

Multipty(a,b)

def outPut():
    return


