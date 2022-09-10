import Funcs as f


A=[
    [1,13,13],
    [5,11,6],
    [4,4,9],
]


rowSum=f.ColumnWiseSum(A)
colsum=f.RowWiseSum(A)
print('Row-Wise: ',end= '')
for i in rowSum:
    print(i ,end='\n          ')
print('\ncolSum-Wise:',end=' ')
for i in colsum:
    print(i, end=' ')