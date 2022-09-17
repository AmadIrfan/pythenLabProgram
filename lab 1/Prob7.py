from funcs import RowWiseSum
from funcs import ColumnWiseSum

Mat=[
    [1,13,13],
    [5,11,6],
    [4,4,9],
]


rowSum=ColumnWiseSum(Mat)
colsum=RowWiseSum(Mat)
print('Row-Wise: ',end= '')
for i in rowSum:
    print(i ,end='\n          ')
print('\ncolSum-Wise:',end=' ')
for i in colsum:
    print(i, end=' ')