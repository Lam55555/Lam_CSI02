num_elements = int(input("Enter the number of elements in the array: "))

def taoMang():
    arr = []
    for i in range(num_elements):
        values = int(input(f"Enter the input for element {i+1}: "))
        arr.append(values)
    return arr

arr = taoMang()

def count_occurrences_with_negatives(arr):
    if len(arr) <= 1:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    
    range_val = max_val - min_val + 1
    count = [0] * range_val
    
    for el in arr:
        count[el - min_val] += 1 
    
    occurrences = {}
    for i in range(range_val):
        if count[i] > 0: 
            occurrences[i + min_val] = count[i]
    
    return occurrences

occurrences = count_occurrences_with_negatives(arr)

for key, value in occurrences.items():
    print(f"{key} : {value} times.")

