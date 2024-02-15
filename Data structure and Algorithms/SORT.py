s =[4,1,2,32,5,154,321,8,9,10]
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr



def selectionSort(arr):
    if(len(arr) < 2):
        return arr
    else:
    # for i in range(len(arr)):
        #temp = arr[i]
        temp = arr[0]

        for j in range(len(arr)): #for j in range(i+1,len(arr)):
            if(arr[j]<temp):
                temp = arr[j]
        temp ,arr[0] = arr[0],temp
        selectionSort(arr[1:])
    return arr

def insertionsort(arr):
    for i in range(1,len(arr)):
        j = i-1
        while arr[j]>arr[j+1] and j>=0:
            arr[j+1] , arr[j] = arr[j],arr[j+1]
            j-=1
    return arr
    # when data is almost sorted or input is small

def mergesort(arr):
    res = []
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        arr1 = mergesort(arr[mid:])
        arr2 = mergesort(arr[:mid])
        i = 0
        j = 0
        while i<len(arr1) and j<len(arr2):
            if(arr1[i]<=arr2[j]):
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        if i<len(arr1):
            res+= arr1[i:]
        elif j<len(arr2):
            res+= arr2[j:]

    return res
    # o(nlog n) ave best and worst time and O(n) space
def quicksort(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[0]
        less = [arr[i] for i in range(1,len(arr)) if arr[i]<=pivot]
        more = [arr[i] for i in range(1,len(arr)) if arr[i]>pivot]
        return quicksort(less) + [pivot] + quicksort(more)
    # o(nlog n) ave best o(n^2) worst time and O(log n) space
print(s)
print(bubble(s))
print(insertionsort(s))
print(selectionSort(s))
print(mergesort(s))
print(quicksort(s))