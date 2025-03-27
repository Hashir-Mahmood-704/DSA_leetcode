# Q4: Count number of zero and one


def count_zero_one(array):
    zero_count = 0
    one_count = 0
    i = 0
    while i < len(array):
        if array[i] == 0:
            zero_count = zero_count + 1
        elif array[i] == 1:
            one_count = one_count + 1
        i = i + 1
    print("Zero count:", zero_count, "One count:", one_count)


count_zero_one([0, 0, 1, 1, 0, 0])
