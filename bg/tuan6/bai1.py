def taomang():
    pt  = int(input("Nhap so phan tu cua mang: "))
    arr = []
    for i in range(0, pt):
        val = int(input(f"Nhap gia tri thứ {i+1}: "))
        arr.append(val)
    return arr


arr = taomang()
#linearSearch

target = int(input("Nhap gia tri can tim: "))

# def linearSearch(target):
#     for i in range(len(a)):
#         if a[i] == target:
#             return i 
#     return -1 

# print(linearSearch(gt))



# Đếm số lần xuất hiện của các phần tử trong danh sách.
# def count_values(arr):
#     b = set(arr)  
#     for i in b:
#         count = 0 
#         for j in arr:
#             if i == j:
#                 count += 1
#         print(f'{i} xuất hiện {count} lần')

# timpt(arr)

# Viết hàm tìm tất cả các vị trí của một phần tử trong danh sách
def demvitriphantu(arr, target): 
    vitri = [] 
    for i in range(len(arr)):
        if arr[i] == target:
            vitri.append(i)
    return vitri
print(demvitriphantu(arr,target))