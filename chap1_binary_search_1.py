# Binary Search needs to receive an Ordered list to accomplish its goal. This search starts at the middle of a list
# and eval if the middle value is equals, minor or major that middle value and depending it, it will move to left (minor)
# or right (major) until the eval is true and return the middle element.
def binary_search(list, item):
    print("searching into the list the item with value " + str(item))
    low = 0
    high = len(list)-1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high)//2 #To receive an integer, divide using double slash. Otherwise you'll recive a float. 
        guess = list[mid]
        if(guess == item):
            print('Value was encountered after ' + str(steps) + ' steps')
            return mid

        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Using Big O Notation, we can calculate the numbers of operations using Logarithms with base 2
#e.g. If a have an "ordered" list of sixteen elements (like above), this algorithm will take
#as maximum (worst-case scenario) 4 steps ,due log(16) = 2
index_founded = binary_search(my_list, 15)

if(index_founded != None):
    print("Item encountered in the list at index " + str(index_founded))
else:
    print("Item was not found in the list")
