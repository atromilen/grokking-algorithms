def binarySearchRecursive(list, item):
    if len(list) == 1:
        return true if (list[0] == item) else false
    else:
        mid = len(list)//2
        guess = list[mid]

        if item == guess:
            return guess

        if item > guess:
            return binarySearchRecursive(list[mid+1:], item)
        elif item < guess:
            return binarySearchRecursive(list[0:mid], item)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
itemFound = binarySearchRecursive(my_list, 6)

if(itemFound):
    print("Item encountered in the list")
else:
    print("Item was not found in the list")