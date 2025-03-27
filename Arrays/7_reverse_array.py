# Q7: Reverse the given array


def swap_elements(array, index1, index2):
    if index1 >= len(array) or index2 >= len(array):
        raise IndexError('Error! Index out of range')
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def reverse_array(array):
    i = 0
    j = len(array) - 1
    while i < j:
        swap_elements(array, i, j)
        i = i + 1
        j = j - 1


array = [10, 20, 30, 40, 50]
reverse_array(array)
print('Reversed array:', array)
