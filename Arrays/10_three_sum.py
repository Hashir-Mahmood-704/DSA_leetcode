# Q10: Find triplets whose sum is equal to target (three sum)

def three_sum(array, target):
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            while k < len(array):
                if array[i] + array[j] + array[k] == target:
                    print(array[i], array[j], array[k])
                k = k + 1
            j = j + 1
        i = i + 1


three_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 10)
