# # queue = [1,2,3,4]
# # front = queue.pop(0)
# # print(front)

# class BrowserHistory:
#     def __init__(self):
#         self.back = []
#         self.forward = "https://www.thegioididong.com/"
#         self.current = "https://www.google.com/search?q=tgdd&rlz=1C1YTUH_viVN1048VN1048&oq=tgdd&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQBRhA0gEHOTczajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8"
#     def visitPage(self, page):
#         self.back.append(self.current)
#         self.current = self.forward
#         self.forward.clear()
#         print(f"Trang hien tai la {page}")
#     def go_back(self):
#         if not self.back:
#             print("Khong con trang")
#         else:
#             self.current = self.back
#             self.forward.append(self.current)
#             print(f"Quay lai trang {self.current}")
#     def go_forward(self):
#         if not self.forward:
#             print("Khong con trang")
#         else:
#             self.current = self.forward
#             self.back.append(self.current)
#             print(f"Trang hien tai {self.current}")
#     def show_current(self):
#         print(f"Trang hien tai la: {self.current}")
#     def run(self):
#         while True:
#             self.show_current()
#             print("1. Truy cập trang mới\n2. Quay lại\n3. Tiến tới\n4. Thoát")
#             choice = int(input("Lua chon cua ban: "))
#             if choice == 1:
#                 new_page =  

class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit_page(self, item):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = item
        self.forward_stack = []

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_page)
            self.current_page = self.back_stack.pop()
        return self.current_page

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_page)
            self.current_page = self.forward_stack.pop()
        return self.current_page
#example
if __name__ == "__main__":
    my_browser = Browser()
    
    my_browser.visit_page("www.example1.com")
    my_browser.visit_page("www.example2.com")
    
    print(my_browser.back())  
    print(my_browser.back())  
    
    print(my_browser.forward())