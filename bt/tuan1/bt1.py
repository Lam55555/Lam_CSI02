
# Bài 1

# first_name = input("First name: ")
# middle_name = input("Middle name: ")
# last_name = input("Last name: ")
# print(f"Output: {first_name} {middle_name} {last_name}")


#Bài 2

# arr = [] 
# nhapsoptmang = int(input("Nhập số phần tử của mảng: "))
# if nhapsoptmang <= 1:
#     print("Khong co so lon thu 2")
# else:
#     for i in range(nhapsoptmang):
#         value = int(input("Input value: "))
#         arr.append(value)
#     mang_bo_trung = set(arr) 
#     mdn = list(reversed(list(mang_bo_trung)))
#     print("So lon thu hai la:", mdn[1])



# Bài 3
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
#     def area(self):
#         return self.width * self.height

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

# def shapes_calculator():
#     a = float(input("Enter side of square (a): "))
#     b = float(input("Enter width of rectangle (b): "))
#     c = float(input("Enter height of rectangle (c): "))

#     square = Square(a)
#     rectangle = Rectangle(b, c)

#     print(f"Square Perimeter: {square.perimeter()}")
#     print(f"Square Area: {square.area()}")
#     print(f"Rectangle Perimeter: {rectangle.perimeter()}")
#     print(f"Rectangle Area: {rectangle.area()}")

# shapes_calculator()


#Bài 4
a = float(input("Enter a number: "))
if a.is_integer():
    print("Integer")
else:
    print("Not integer")
