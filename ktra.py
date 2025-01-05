# import time
 


# # Bài 1
# # chuoi = input("Nhap chuoi khong qua 20 ky tu: ")
# # if len(chuoi) <= 20:
# #     w = chuoi.split()
# #     print(w)
# # else:
# #     print("Da nhap qua 20 ky tu")

# # Bài 2

# import time

# # Hàm tạo mảng
# def taoMang():
#     a = []
#     sopt = int(input("Nhập số lượng phần tử của mảng: "))
#     for i in range(sopt):
#         val = int(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
#         a.append(val)
#     return a

# # Selection Sort
# def find_min(data_list, from_index):
#     min_ind = from_index
#     for i in range(from_index + 1, len(data_list)):
#         if data_list[i] < data_list[min_ind]:
#             min_ind = i
#     return min_ind

# def selection_sort(data_list):
#     comparisons = 0
#     start_time = time.time()
#     for i in range(len(data_list) - 1):
#         min_ind = find_min(data_list, i)
#         comparisons += len(data_list) - i - 1  
#         if min_ind != i:
#             data_list[i], data_list[min_ind] = data_list[min_ind], data_list[i]
#     elapsed_time = time.time() - start_time
#     return data_list, comparisons, elapsed_time

# # Insertion Sort
# def insertion_sort(arr):
#     comparisons = 0      
#     start_time = time.time()  
#     for i in range(1, len(arr)):
#         j = i 
#         while j > 0 and arr[j] < arr[j - 1]:
#             comparisons += 1
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1
#         if j > 0:
#             comparisons += 1
#     elapsed_time = time.time() - start_time 
#     return arr, comparisons,  elapsed_time

# # Bubble Sort
# def bubble_sort(arr):
#     comparisons = 0   
#     start_time = time.time()  
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             comparisons += 1
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     elapsed_time = time.time() - start_time 
#     return arr, comparisons,  elapsed_time

# data = taoMang()

# data_selection = data.copy() 
# sorted_data, comparisons, elapsed_time = selection_sort(data_selection)
# print("Selection Sort:")
# print("Mảng sau khi sắp xếp:", sorted_data)
# print(f"Số lần so sánh: {comparisons}")
# print(f"Thời gian thực thi: {elapsed_time:.6f} giây")


# data_insertion = data.copy()
# sorted_data, comparisons, elapsed_time = insertion_sort(data_insertion)
# print("\nInsertion Sort:")
# print("Mảng sau khi sắp xếp:", sorted_data)
# print(f"Số lần so sánh: {comparisons}")
# print(f"Thời gian thực thi: {elapsed_time:.6f} giây")

# data_bubble = data.copy()
# sorted_data, comparisons, elapsed_time = bubble_sort(data_bubble)
# print("\nBubble Sort:")
# print("Mảng sau khi sắp xếp:", sorted_data)
# print(f"Số lần so sánh: {comparisons}")
# print(f"Thời gian thực thi: {elapsed_time:.6f} giây")