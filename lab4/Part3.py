
def printMatrix(A,starting_index,rows,columns):
    sIndex=starting_index[0]
    lIndex=starting_index[1]
    for i in range(sIndex,rows):
        for j in range(lIndex,columns):
            print(A[i][j],end=' ')
        print()


Matrix=[]
new=[]
for i in range(1): 
    n_rows= int(input("Number of rows:"))
    n_cols = int(input("Number of columns:"))
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix.append(a)


        
starting=int(input("Enter starting index x "))
Ending=int(input("Enter starting index y "))
end=[starting,Ending]
tup=tuple(end)
printMatrix(Matrix,tup,2,2)


def MatAdd(A,B):
    total=[]
    add=0
    for i in range(len(A)):
        sum=[]
        for j in range(len(B[0])):
            add=A[i][j]+B[i][j]
            sum.append(add)
        total.append(sum)
    for i in range(len(total)):
        for j in range(len(total[0])):
            print(total[i][j],end=' ')
        print()


print('Sum of two Matrixs')
print('Matrix 1')
Matrix0=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix A ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix0.append(a)

print('Enter Matrix 2 ')
Matrix1=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix B ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix1.append(a)
MatAdd(Matrix0, Matrix1)


def MatMul(A,B):
    total=[]
    for i in range(len(A)):
        a=[]
        for j in range(len(B)):
            a.append(0)
        total.append(a)
            
    for i in range(len(A)):
        for j in range(len(B)):
            sum=0
            for k in range(len(A)):
                sum+=A[i][k]*B[k][j]
            total[i][j]=sum
    print('Products of two Matrixs')
    for i in total:
        a=[]
        for j in i:
            print(j,end=' ')
        print()


print('Products of two Matrixs')

print('Enter Matrix 1')
Matrix0=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix A ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix0.append(a)


print('Enter Matrix 2 ')
Matrix1=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix B ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix1.append(a)
MatMul(Matrix0, Matrix1)


print('sum of two Partial Matrixs')

def MatAddPartial(A, B, start, size):
    add=0
    s=start[0]
    e=start[1]
    for i in range(s,size):
        for j in range(e,size):
            add=A[i][j]+B[i][j]
            print(add,end=' ')
        print()
        
        

    
print('Enter Matrix 1')
Matrix0=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix A ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix0.append(a)
print('Enter Matrix 2 ')
Matrix1=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix B ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix1.append(a)
starting=int(input("Enter starting index x "))
Ending=int(input("Enter ending index y "))
end=[starting,Ending]
start=tuple(end)
size=int(input("Enter size "))
MatAddPartial(Matrix0, Matrix1, start, size)

print("MatMulStrassen ")
def MatMulStrassen(A,B):
    print(A,B)


print("MatMulrecursion ")
def MatMulRecursive(A,B):
    print(A,B)


print('Enter Matrix 1')
Matrix0=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix A ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix0.append(a)
print('Enter Matrix 2 ')
Matrix1=[]
for i in range(1): 
    n_rows= int(input("Number of rows: "))
    n_cols = int(input("Number of columns: "))
    print('Enter element of Matrix B ')
    for i in range(n_rows):
        a =[]
        for j in range(n_cols):
            a.append(int(input()))
        Matrix1.append(a)
        
MatMulRecursive(Matrix0, Matrix1)
MatMulStrassen(Matrix0, Matrix1)