num_elements = int(input("Enter the number of elements in the array: "))

def create_array():
    array = []
    for i in range(0, num_elements):
        value = int(input(f"Enter the input for element {i+1}: "))
        array.append(value)
    return array

arr = create_array()

def bubble_sort(arr):
    arr_length = len(arr)
    swap_count = 0
    for i in range(0, arr_length):
        for j in range(0, arr_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return swap_count

swap_count = bubble_sort(arr)

print(f"Sorted Array: {arr}")
print(f"Swap count: {swap_count}")
