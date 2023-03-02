""" 
movies = [] # biến toàn cục

# def my_func():
#     movies.append("abc")
#     print(movies)

def my_func():
    global movies  # khi gọi hàm biến sẽ được tạo ra và là biến toàn cục
    # biến cục bộ sau khi gọi hàm sẽ biến mất và không được định nghĩa bên ngoài
    movies = ["Hi"]
    movies.append("abc")
    print(movies)


# my_func()  # ['Hi', 'abc']
# my_func()  # ['Hi', 'abc']
# print(movies)  # ['Hi', 'abc']

my_func() # ['Hi', 'abc']
my_func()# ['Hi', 'abc']
print(movies)# ['Hi', 'abc']

"""
""" 
def delete():
    global lst
    lst = [x for x in lst if x != "a"]
lst = ['a', 'b', 'a', 'a', 'd']

# for x in lst:
#     if x == "a":
#         lst.remove(x)

# print(lst)  # khác chỉ số lên sẽ không xoá hết 'a'    ['b', 'a', 'd']  

# không thể vừa duyệt vừa xoá

# new_lst = [x for x in lst if x != "a"]
# print(new_lst)
delete()
print(lst)
 """

# không thể sử dụng tab và space