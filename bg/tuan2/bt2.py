# arr_1 = [] 
# arr_2 = []
# nhapsoptmang_1 = int(input("Nhập số phần tử của mảng 1: "))

# for i in range(nhapsoptmang_1):
#     value_1 = int(input("Input a value: "))
#     arr_1.append(value_1) 
# nhapsoptmang_2 = int(input("Nhập số phần tử của mảng 2: "))    
# for i in range(nhapsoptmang_2):
#     value_2 = int(input("Input a value: "))
#     arr_2.append(value_2) 
# arr_1.extend(arr_2)
# arr_1.reverse()
# print(arr_1)




# arr1 = [int(x) for x in input('Nhập số').split() ]
# arr2 = [int(x) for x in input('Nhập số').split() ]

# all = arr1 + arr2
# all.sort(reverse=True)
# print("Dãy số sau khi kết hợp và sắp xếp giảm dần:")
# print(all)


# import numpy as np
# x = int(input("Enter number of the starting point of the range you want for the first list: (from) "))
# y = int(input("Enter number of the ending point of the range you want for the first list: (to) "))
# n = int(input("Enter number of numbers you want for the first list: "))
# a = int(input("Enter number of the starting point of the range you want for the second list: (from) "))
# b = int(input("Enter number of the ending point of the range you want for the second list: (to) "))
# m = int(input("Enter number of numbers you want for the second list: "))
# arr1 = np.random.randint(x,y,n).tolist()
# arr2 = np.random.randint(a,b,m).tolist()
# for i in arr2:
#     arr1.append(i)
# arr1.sort(reverse=True)
# print(arr1)