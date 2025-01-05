# arr = [2,6,2,1]
# index_1 = 0
# index_2 = len(arr)-1
# arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

# print(arr)


def count_swap(arr):
    count = 0
    max_len = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] > arr[max_len]:
            arr[i], arr[max_len] = arr[max_len], arr[i]
            count += 1 
    return count

try:
    assert(count_swap([2, 5, 3, 1]) == 2)
    print('Correct answer on sample test!')
except:
    print('Invalid submission or Wrong answer!')

