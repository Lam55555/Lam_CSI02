arr = [] 
nhapsopt = int(input("Nhập số phần tử: "))

for i in range(nhapsopt):
    value_1 = int(input("Input a value: "))
    arr.append(value_1) 
tup = tuple(arr)
result = (max(tup), min(tup), sum(tup)/len(tup))
print(result)