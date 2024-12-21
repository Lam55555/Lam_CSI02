num_elements = int(input("Enter the number of elements in the array: "))
def taoMang():
    arr = []
    for i in range(0,num_elements):
        values = int(input(f"Enter the input for element {i+1}: "))
        arr.append(values)
    return arr
arr = taoMang()

def binarySrch(target):
    mang = arr
    left = 0
    right = len(mang)-1
    while left <= right:
        mid = (left + right)//2
        if mang[mid] > target:
            right = mid-1
        elif mang[mid] < target:
            left = mid+1
        elif mang[mid] == target:
            return mid
    
target = int(input("Enter the target element to find: "))
print(binarySrch(target))