def binary_search(list, item):
    print("searching into the list the item with value " + str(item))
    low = 0
    high = len(list)-1
    count = 0

    while low <= high:
        count += 1
        print("Iteration number " + str(count))
        mid = (low + high)//2 #To receive an integer, it's necessary to use //
        guess = list[mid]

        print("mid: " + str(mid))
        print("guess: " + str(guess))

        if(guess == item):
            return mid

        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

#Using Big O Notation, I can calculate the numbers of iteration using Logarithms with base 2
#e.g. If a have an "ordered" list of sixteen elements (like above), this algorithm will take
#like maximum (in the worst of cases) 4 steps (due log(16) = 2)
index_founded = binary_search(my_list, 31)

if(index_founded != None):
    print("The item was encountered at the position " + str(index_founded))
else:
    print("The item was not found in the list")
