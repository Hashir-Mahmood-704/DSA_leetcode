# Q14: Right rotate array by given places

def swap_elements(array, index1, index2):
    if index1 >= len(array) or index2 >= len(array):
        raise IndexError('Error! Index out of range')
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def rightRotate(array, rotate):
    rotate = rotate % len(array)
    if rotate == 0:
        print("rotated array", array)
        return

    i = 0
    j = len(array) - rotate - 1
    while i < j:
        swap_elements(array, i, j)
        i = i + 1
        j = j - 1

    i = len(array) - rotate
    j = len(array) - 1
    while i < j:
        swap_elements(array, i, j)
        i = i + 1
        j = j - 1

    i = 0
    j = len(array) - 1
    while i < j:
        swap_elements(array, i, j)
        i = i + 1
        j = j - 1

    print("right rotated array", array)


rightRotate([1, 2, 3, 4, 5], 1)
