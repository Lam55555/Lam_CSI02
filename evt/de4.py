import time as t

start = t.time()
for i in range(1000000):
    pass
end = t.time()
print("thoi gian chay", end-start)

n = int(input('Số lượng hệ thống bơm nước: '))
kc = list(map(int, input('Nhập khoảng cách: ').split()))
td = list(map(int, input('Nhập tốc độ: ').split()))

tg = 0
for d, s in zip(kc, td):
    if s != 0:
        tg += d / s
    else:
        print(-1)
        break
else:
    print(f'{tg} giờ')