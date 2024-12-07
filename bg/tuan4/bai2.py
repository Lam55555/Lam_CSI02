def taoMang():
    a = []
    sopt = int(input("Nhập số lượng phần tử của mảng: "))
    for i in range(sopt):
        val = int(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
        a.append(val)
    return a

def binaryArr(a, target):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right)//2 
        if a[mid] == target:
            print(f"Giá trị {target} được tìm thấy ở vị trí {mid}")
            return
        elif a[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1


    print("Không tìm thấy giá trị này trong mảng.")

a = taoMang()
a.sort() 
target = int(input("Nhập giá trị cần tìm: "))
binaryArr(a, target)
