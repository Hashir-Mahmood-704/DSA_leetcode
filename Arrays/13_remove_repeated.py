# Q13: Remove repeated elements from sorted array


def swap_elements(array, index1, index2):
    if index1 > len(array) - 1 or index2 > len(array) - 1:
        raise IndexError("Error! Index out of range")
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def remove_repeated_from_sorted_array(array):
    i = 0
    j = 1
    while j < len(array):
        if array[i] != array[j]:
            i = i + 1
            swap_elements(array, i, j)
        j = j + 1
    print("Number of unique elements:", i + 1)


array = [1, 2, 2, 3, 4, 4, 4, 5]
remove_repeated_from_sorted_array(array)
print(array)
