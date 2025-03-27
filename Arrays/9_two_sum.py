# Q9: Find two sum pairs whose sum is equal to target from array


def two_sum(array, target):
    array.sort()  # sorts in ascending order by default
    i = 0
    j = len(array) - 1
    while i < j:
        current_sum = array[i] + array[j]
        if current_sum == target:
            print(array[i], array[j])
            i = i + 1
            j = j + 1
        elif current_sum < target:
            i = i + 1
        else:
            j = j - 1


two_sum([1, 2, 3, 4, 6, 7, 11, 15], 10)






