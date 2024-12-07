import time as t

start = t.time()
for i in range(1000000):
    pass
end = t.time()
print("thoi gian chay", end-start)


def xoa_trung(s):
    chuoi_kq = ""
    for char in s:
        if char not in chuoi_kq:
            chuoi_kq += char
    return chuoi_kq
chuoi = input("Nhap chuoi: ")
print(xoa_trung(chuoi))

