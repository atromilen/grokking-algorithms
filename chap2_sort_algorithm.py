def findSmallest(arr):
    smallest = arr[0] 
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_idx = findSmallest(arr)
        newArr.append(arr.pop(smallest_idx))
    return newArr

unsorted_array = [5, 3, 6, 2, 10]
print(unsorted_array)
sortedArray = selectionSort(unsorted_array)
print(sortedArray)

