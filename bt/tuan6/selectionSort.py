num_elements = int(input("Enter the number of elements in the array: "))
def create_Array():
    arr = []
    for i in range(num_elements):
        values = int(input(f"Enter the input for element {i + 1}: "))
        arr.append(values)
    return arr

arr = create_Array()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(f"Sorted Array: {selection_sort(arr)}")