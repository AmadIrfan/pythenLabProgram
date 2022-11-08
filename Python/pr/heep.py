from math import *


def Left(i):
    return 2*i


def right(i):
    return (2*i)+1


def Parent(i):
    return floor(i/2)


def MaxHeapify(Arr, i):
    l = Left(i)
    r = right(i)
    if l <= Arr.heapSize and Arr[l] < Arr[i]:
        largest = l
    else:
        largest = i

    if r < Arr.heapSize and Arr[r] < Arr[largest]:
        largest = r
    if (largest != i):
        temp = Arr[largest]
        Arr[largest] = Arr[i]
        Arr[i] = temp
    MaxHeapify(Arr, largest)


def Build_Max_Heap(A):
    A.heapSize = A.length
    for i in reversed(range(1, len(A)/2)):
        MaxHeapify(A, i)


def heapSort(A):
    Build_Max_Heap(A)
    for i in reversed(range(2, len(A))):
        A[1], A[i] = A[i], A[1]
        A.heapSize = A.heapSize-1
        MaxHeapify(A, i)


def heap_max_extrect(A):
    if A.heapSize < 1:
        Exception('heep underflow')
    max = A[1]
    A[1] = A[A.heapSize]
    A.heapSize = A.heapSize-1
    MaxHeapify(A, 1)
    return max


def heapIncreaseKey(A, i, key):
    if key < A[i]:
        print('error')
        A[i] = key
        while i > 1 and A[Parent(i)] < A[i]:
            A[i], A[Parent(i)] = A[Parent(i)], A[i]
            i = Parent(i)


def max_heap_insert(A, key):
    A.heapSize = A.heapSize+1
    A[A.heapSize] = -1999999999
    heapIncreaseKey(A, A.heapSize, key)
