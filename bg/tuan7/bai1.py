num_elements = int(input("Enter the number of elements in the array: "))

def taoMang():
    arr = []
    for i in range(num_elements):
        values = int(input(f"Enter the input for element {i+1}: "))
        arr.append(values)
    return arr

arr = taoMang()

def partition(arr, left, right):
    pivot = arr[left]
    i = left  
    for j in range(left + 1, right):  
        if arr[j] < pivot:
            i += 1  
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i], arr[left] = arr[left], arr[i]  
    return i  

def quick_sort(arr, left, right):
    if right - left <= 1: 
        return
    partition_index = partition(arr, left, right)  
    quick_sort(arr, left, partition_index)  
    quick_sort(arr, partition_index + 1, right) 


quick_sort(arr, 0, len(arr))
print("Sorted array:", arr)
