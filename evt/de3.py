import time as t

start = t.time()
for i in range(1000000):
    pass
end = t.time()
print("thoi gian chay", end-start)

def dem_cay(n, arr, x):
    count = 0
    for water in arr:
        if water >= x:
            count += 1
    return count

n = int(input("Nhập số lượng cây: "))
arr = list(map(int, input("Nhập lượng nước mỗi cây cần: ").split()))
x = int(input("Nhập lượng nước tối thiểu cần: "))

result = dem_cay(n, arr, x)
print(result)
