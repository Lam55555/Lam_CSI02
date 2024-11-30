def taoMang():
    a = []
    sopt = int(input("Nhập số lượng phần tử của mảng: "))
    for i in range(sopt):
        val = int(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
        a.append(val)
    return a

a = taoMang()
gtri = int(input("Nhập giá trị cần tìm: "))

def timKiemTuanTu(a, gtri):
    for i in range(len(a)):
        if gtri == a[i]:
            return print(f"Giá trị {gtri} được tìm thấy ở vị trí {i}")
    return print("Không tìm thấy giá trị này trong mảng.")

timKiemTuanTu(a, gtri)

