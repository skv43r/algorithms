def findSmalliest(arr):
    smalliest = arr[0]
    smalliest_index = 0
    for i in range(len(arr)):
        if arr[i] < smalliest:
            smalliest = arr[i]
            smalliest_index = i
    return smalliest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmalliest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(*selectionSort([4, 6, 1, 12, 5, 18, 43, 943, 11, 52, 22, 21, 19]))            