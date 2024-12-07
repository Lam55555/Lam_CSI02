import time as t

start = t.time()
for i in range(1000000):
    pass
end = t.time()
print("thoi gian chay", end-start)
def tim_group(arr, k):
    a = []
    so_tv = {}
    for num in arr:
        if num == k:
            a.append(num)
    for num in arr:
        compl = k - num
        if so_tv.get(compl, 0) > 0:
            a.append((num, compl))
            so_tv[compl] -= 1
        else:
            so_tv[num] = so_tv.get(num, 0) + 1 
    return a


n = int(input("Nhap so luong phan tu: "))
arr = list(map(int, input("Nhap cac phan tu cua mang (cach nhau boi dau cach): ").split()))
k = int(input("Nhap tong so can tim: "))
print(tim_group(arr, k))