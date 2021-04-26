# 4.1 Write out the code for the earlier sum function (recursive)
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

# 4.2 Write a recursive function to count the number of items in a list
def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])

# 4.3 Fin the maximum number in a list
def findMaximum(list):
    if len(list) == 2:
        return list[0] if (list[0] > list[1]) else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max


list = [1,2,3,4,5]

print('4.1 Write out the code for the earlier sum function (recursive)')
print('Sum of {} is: {}'.format(list, sum(list)))

print('4.2 Write a recursive function to count the number of items in a list')
print('Items on {} are: {}'.format(list, count(list)))

print('4.3 Fin the maximum number in a list')
newList = [2,3,5,1,9,12,21,4,6]
print('maximum of {} is: {}'.format(newList, findMaximum(newList)))