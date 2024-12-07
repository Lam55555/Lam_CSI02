import math
import time as t

start = t.time()
for i in range(1000000):
    pass
end = t.time()
print("thoi gian chay", end-start)

def calculate_ways(n, tnt):
    tainguyenconlai = tnt - n
    if tainguyenconlai < 0:
        return 0
    return math.comb(tainguyenconlai + n - 1, n - 1)

n = int(input("Nhap so nhom: "))
total = int(input("Nhap so tai nguyen: "))

print(f'có {calculate_ways(n, total)} cách')
