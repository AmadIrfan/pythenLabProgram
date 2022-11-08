import random

arr = []
for i in range(0, 10):
    arr.append(random.randint(0, 10))

print(arr)
def Partition(A, p, r):
    pivet = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= pivet):
            i=i+1
            tp1 = A[j]
            A[j] = A[i]
            A[i] = tp1
    tp2 = A[r]
    A[r] = A[i+1]
    A[i+1] = tp2
    return i+1


def QuickSort(Arr, p, r):
    if (p < r):
        q = Partition(Arr, p, r)
        QuickSort(Arr, p, q-1)
        QuickSort(Arr, q+1, r)
    return Arr


print(QuickSort(arr, 0, len(arr)-1))

