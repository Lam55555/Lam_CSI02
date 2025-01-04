num_elements = int(input("Enter the number of elements in the array: "))

def taoMang():
    arr = []
    for i in range(num_elements):
        values = int(input(f"Enter the input for element {i+1}: "))
        arr.append(values)
    return arr

arr = taoMang()

def counting_sort(arr):
    if len(arr) <= 1:
        return arr  

    min_val = min(arr)
    max_val = max(arr)
    

    range_val = max_val - min_val + 1
    count = [0] * range_val
    

    for el in arr:
        count[el - min_val] += 1
    
    index = 0
    for i in range(range_val):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1

    return arr

sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
