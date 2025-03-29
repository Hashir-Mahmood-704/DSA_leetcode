# Q21: Sort 0, 1, 2 in array in ascending order


def swap_elements(array, index1, index2):
    if index1 >= len(array) or index2 >= len(array):
        raise IndexError("Error! Index out of range")
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def sortZeroOneTwo(array):
    l = 0
    m = 0
    h = len(array) - 1
    while m <= h:
        if array[m] == 0:
            swap_elements(array, l, m)
            l = l + 1
            m = m + 1
        elif array[m] == 1:
            m = m + 1
        else:
            swap_elements(array, m, h)
            h = h - 1
    print(array)


sortZeroOneTwo([2, 0, 1, 2, 1, 1, 0, 2])
