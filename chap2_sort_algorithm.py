# The Selection Sort algorithm needs to iterate in over element in the array to encounter the smallest index in a list.
# After each iteration, the smallest index is removed and the remainder elements are passed to a new smallest index search,
# until the list only have 1 element and all the elements were ordered in a new list.


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
print('Sorting the array with elements {}'.format(unsorted_array))
sortedArray = selectionSort(unsorted_array)
print(sortedArray)

