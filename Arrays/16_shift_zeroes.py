# Q16: Shift all zeroes in array to end

def swap_elements(array, index1, index2):
    if index1 >= len(array) or index2 >= len(array):
        raise IndexError('Error! Index out of range')
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def shiftZeroes(array):
    i = -1
    j = 0
    while j < len(array):
        if array[j] > 0:
            i = i + 1
            swap_elements(array, i, j)
        j = j + 1
    print(array)


shiftZeroes([0, 1, 2, 0, 0, 3, 0])
