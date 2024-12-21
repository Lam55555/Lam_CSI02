num_elements = int(input("Enter the number of elements in the array: "))

def create_Array():
    arr = []
    for i in range(0,num_elements):
        values = int(input(f"Enter the input for element {i+1}: "))
        arr.append(values)
    return arr

arr = create_Array()

def insertion_sort(arr):
    for i in range(1, len(arr)): 
        current_value = arr[i] 
        j = i - 1 
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = current_value
    return arr

print(f"Sorted Array: {insertion_sort(arr)}")



