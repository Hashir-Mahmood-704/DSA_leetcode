 # Q11: Rotate a given array.
 # for example: input = [1, 2, 3, 4, 5] and rotate = 3, then result = [4, 5, 1, 2, 3]

def rotate_array(array, rotate):
    n = len(array)
    rotate = rotate % n
    if rotate == 0 or rotate == n:
        return

    temp_array = [None] * rotate
    i = n - rotate
    j = 0
    while i < n:
        temp_array[j] = array[i]
        i = i + 1
        j = j + 1

    i = n - 1
    while i - rotate > -1:
        array[i] = array[i - rotate]
        i = i - 1

    i = 0
    while i < len(temp_array):
        array[i] = temp_array[i]
        i = i + 1

array = [1, 2, 3, 4, 5, 6, 7]
rotate_array(array, 3)
print('Rotated array:', array)
