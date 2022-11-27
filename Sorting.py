import SongBL
import SongsDL


def InsertionSort(Array, mode):
    for i in range(0, len(Array)):
        key = Array[i]
        j = i-1
        if mode == "Ascending":
            while (key < Array[j] and j >= 0):
                Array[j+1] = Array[j]
                SongsDL.songsList[j+1] = SongsDL.songsList[j]
                j = j-1
            Array[j+1] = key
        if mode == "Descending":
            while (key > Array[j] and j >= 0):
                Array[j+1] = Array[j]
                SongsDL.songsList[j+1] = SongsDL.songsList[j]
                j = j-1
            Array[j+1] = key
            
SongsDL.Loaddata()
allLists = SongsDL.sepratelists()
# InsertionSort(allLists[4])
print("--------------------------------------")

################################  QUICK SORT ######################################################


def quickSort(array, low, high, mode):
    if low < high:
        pi = partition(array, low, high, mode)
        quickSort(array, low, pi - 1, mode)
        quickSort(array, pi + 1, high, mode)


def partition(array, low, high, mode):
    pivot = array[high]

    i = low - 1
    if mode == "Asc":
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (SongsDL.songsList[i], SongsDL.songsList[j]) = (
                    SongsDL.songsList[j], SongsDL.songsList[i])

    if mode == "Des":
        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (SongsDL.songsList[i], SongsDL.songsList[j]) = (
                    SongsDL.songsList[j], SongsDL.songsList[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    (SongsDL.songsList[i + 1], SongsDL.songsList[high]
     ) = (SongsDL.songsList[high], SongsDL.songsList[i + 1])

    return i + 1


print("--------------------------------------")
#quickSort(allLists[4], 0, len(allLists[4])-1, "Asc")

# for s in SongsDL.songsList:
#print(s.name,s.album,s.genre,s.Likes, s.duration, s.Comments, s.year)


#####################   Merge Sort  ################################################

def Merge(arr, p, q, r, mode):
    if mode == "Ascending":
        n1 = q - p + 1
        n2 = r - q
        L = [0] * (n1)
        tempL = [0]*(n1)
        R = [0] * (n2)
        tempR = [0]*(n1)

        for i in range(0, n1):
            L[i] = arr[p + i]
            tempL[i] = SongsDL.songsList[p+i]
        for j in range(0, n2):
            R[j] = arr[q + 1 + j]
            tempR[j] = SongsDL.songsList[q+1+j]
        i = 0
        j = 0
        k = p

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                SongsDL.songsList[k] = tempL[i]
                i += 1
            else:
                arr[k] = R[j]
                SongsDL.songsList[k] = tempR[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            SongsDL.songsList[k] = tempL[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            SongsDL.songsList[k] = tempR[j]
            j += 1
            k += 1
    else:
        n1 = q - p + 1
        n2 = r - q
        L = [0] * (n1)
        tempL = [0]*(n1)
        R = [0] * (n2)
        tempR = [0]*(n1)

        for i in range(0, n1):
            L[i] = arr[p + i]
            tempL[i] = SongsDL.songsList[p+i]
        for j in range(0, n2):
            R[j] = arr[q + 1 + j]
            tempR[j] = SongsDL.songsList[q+1+j]
        i = 0
        j = 0
        k = p
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = R[j]
                SongsDL.songsList[k] = tempR[j]
                j += 1
            else:
                arr[k] = L[i]
                SongsDL.songsList[k] = tempL[i]
                i += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            SongsDL.songsList[k] = tempL[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            SongsDL.songsList[k] = tempR[j]
            j += 1
            k += 1
        if p < q:
            m = p+(q-p)//2
            MergeSort(arr, p, m, mode)
            MergeSort(arr, m+1, q, mode)
            Merge(arr, p, m, q, mode)


def MergeSort(arr, p, q, mode):
    if p < q:
        m = p+(q-p)//2
        MergeSort(arr, p, m, mode)
        MergeSort(arr, m+1, q, mode)
        Merge(arr, p, m, q, mode)

   # return arr
    return arr


allLists = SongsDL.sepratelists()

#print(MergeSort(allLists[6], 0, len(allLists[6])-1, "Ascending"))
# for s in SongsDL.songsList:
#print(s.name,s.album,s.genre,s.Likes, s.duration, s.Comments, s.year)


############################# hybridMerge Sort ######################################################
def HybridMergeSort(A, p, r, mode):
    dif = r - p
    if (p < r and dif > 43):
        q = (p + r)//2
        HybridMergeSort(A, p, r, mode)
        HybridMergeSort(A, p, r, mode)
        Merge(A, p, q, r)
    else:
        InsertionSort(A, mode)


########################################## gnomeSort######################################################
def gnomeSort(arr, n, mode):

    if mode == "Descending":
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if arr[index] <= arr[index - 1]:
                index = index + 1
            else:
                temp = arr[index]
                temp2 = SongsDL.songsList[index]
                arr[index] = arr[index-1]
                SongsDL.songsList[index] = SongsDL.songsList[index-1]
                arr[index-1] = temp
                SongsDL.songsList[index-1] = temp2
                index = index - 1
        return arr
    else:
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                index = index + 1
            else:
                temp = arr[index]
                arr[index] = arr[index-1]
                arr[index-1] = temp
                index = index - 1
        return arr


allLists = SongsDL.sepratelists()

gnomeSort(allLists[6], len(allLists[6]), "Descending")
# for s in SongsDL.songsList:
#    print(s.name,s.album,s.genre,s.Likes,s.playedtime, s.duration, s.Comments, s.year)
################################  Heap Sort ###################################################


def heapify(arr, N, i, mode):
    largest = i
    largest2 = SongsDL.songsList[i]
    l = 2 * i + 1
    l2 = SongsDL.songsList[2 * i + 1]
    r = 2 * i + 2
    r2 = SongsDL.songsList[2 * i + 2]
    if mode == "Ascending":

        if l < N and arr[largest] < arr[l]:
            largest = l

        if r < N and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            # direct swap
            arr[i], arr[largest] = arr[largest], arr[i]
            SongsDL.songsList[i], SongsDL.songsList[largest2], SongsDL.songsList[i]
            heapify(arr, N, largest, mode)
    else:
        if l < N and arr[largest] > arr[l]:
            largest = l

        if r < N and arr[largest] > arr[r]:
            largest = r

        if largest != i:
            # direct swap
            arr[i], arr[largest] = arr[largest], arr[i]
            SongsDL.songsList[i], SongsDL.songsList[largest2], SongsDL.songsList[i]


def buildmaxheapify(arr, mode):
    N = len(arr)
    for i in range(int(N/2) - 1, -1, -1):
        heapify(arr, N, i, mode)


def heapSort(arr, mode):
    buildmaxheapify(arr, mode)
    for i in range(len(arr)-1, 0, -1):
        temp = arr[i]
        temp2 = SongsDL.songsList[i]
        arr[i] = arr[0]
        SongsDL.songsList[i] = SongsDL.songsList[0]
        arr[0] = temp
        SongsDL.songsList[0] = temp2
        heapify(arr, i, 0, mode)


allLists = SongsDL.sepratelists()
#print(heapSort(allLists[6], "Ascending"))


################################# COMB SORT #########################################
def getNextGap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap


def combSort(arr, mode):
    n = len(arr)
    gap = n
    swapped = True
    if mode == "Ascending":
        while gap != 1 or swapped == 1:
            gap = getNextGap(gap)
            swapped = False
            for i in range(0, n-gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    SongsDL.songsList[i], SongsDL.songsList[i +
                                                            gap] = SongsDL.songsList[i+gap], SongsDL.songsList[i]
                    swapped = True
    else:
        while gap != 1 or swapped == 1:
            gap = getNextGap(gap)
            swapped = False
            for i in range(0, n-gap):
                if arr[i] < arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    SongsDL.songsList[i], SongsDL.songsList[i +
                                                            gap] = SongsDL.songsList[i+gap], SongsDL.songsList[i]
                    swapped = True


combSort(allLists[6], "descnending")
for s in SongsDL.songsList:
    print(s.duration, s.Comments, s.year)
