# Bài 1
# def find_mode(arr):
#     if len(arr) <=1:
#         return arr

#     min_val = min(arr)
#     max_val = max(arr)
#     range_val = max_val - min_val + 1
#     count = [0] * range_val
#     for el in arr:
#         count[el - min_val] += 1
#     max_count = max(count)

    
#     modes = [i + min_val for i, c in enumerate(count) if c == max_count]
#     return max(modes)

# try:
#     assert(find_mode([1, 2, 3, 2, 3]) == 3)
#     print('Correct answer on sample test!')
# except:
#     print('Invalid submission or Wrong answer!')

# Bài 2
# def has_sequence_with_sum(target_sum, arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]+arr[j+1] == target_sum:
#                 return True
#     return False
# try:
#     assert(has_sequence_with_sum(8, [1, 5, 3, 2, 5]) == True)
#     print('Correct answer on sample test!')
# except:
#     print('Invalid submission or Wrong answer!')

# Bài 3
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