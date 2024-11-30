tuple_value = (1,2,3,"Hello")
num1 = 13
num2 = 6.3
num3 = 6
# print("Power",(num1**num2))

# print(num1+num2*num3)

# print(((num1+num2)*num3)/14)

# print("Max:", max)

# class Person:
#     race = "human"
#     def __init__(self):
#         pass

# def nhan2(num):
#     return num*2
# a = float(input("Input a number: "))
# print(nhan2(a))

# def double_number():
#     num = float(input("Input a number: "))
#     print(num*2)
# double_number()

# pi = 3.1416
# r = float(input("Nhập bán kính: "))
# def perimeter(cv):
#     return 2*pi*cv
# def area(dt):
#     return pi*dt*dt
# print(perimeter(r))
# print(area(r))
arr = []  # Khởi tạo danh sách rỗng
nhapsoptmang = int(input("Nhập số phần tử của mảng: "))

for i in range(nhapsoptmang):
    value = int(input("Input a value: "))
    arr.append(abs(value))  # Dùng abs() để lưu giá trị tuyệt đối của value vào mảng

num = 0

for i in arr:
    if i % 2 == 0:
        num += i

print("Tổng số chẵn là:", num)


# nhapso = int(input("Nhập số phần tử của mảng: "))
# def taomang(p):
#     b = []
#     for i in range(0, nhapsomang):
#         val = int(input("Input a value: "))
#         if val > 0:
#             b.append(val)
#         else:
#             print("Nhập số lớn hơn không")

# def tongchan():
#     if 

# n = int(input("Please enter the total number of numbers"))
# num_list = []
# odd_list = []

# for i in range(n):
#     a = int(input("Please enter a number"))
#     num_list.append(a)

# for i in num_list:
#     if i % 2 == 0: odd_list.append(i)
    
# print(sum(odd_list))