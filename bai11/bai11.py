# python functions

""" def get_full_name(fname, lname="18"):
    if fname:
        return (f"{fname} {lname}")
    return f"Kenny {lname}"

full_name = get_full_name(lname="a", fname="b") # bool("")=False
print(full_name) """

""" def add(x,y=10):
    return x + y

print(add(x=40, y=100)) """

""" def func(lst=[]): #[] da duoc dinh nghia lst tham chieu 
    # tranh tham so thay doi duoc: list dict
    lst.append(2)
    print(lst)

func()[2]
func()[2,2]  
"""

""" friends = ["a", "b", "c"]

def my_func():
    f = friends + ["d"] # bien cuc bo nam ben trong tuc la friends trong ham khac vs friends ngoai: do friends ben p duoc tham chieu truoc khi duoc tao -> dat ten khac 
    print(f)

my_func()    
"""

"""
 add = lambda x, y: x+y
print(add(1,2)) 
"""

""" def greet(msg):
    print("hi" + msg)
    return None
a = greet
print(a(" b")) """

""" def func():
    pass """  # ham khong dc trong phan than pass de tao ham khong lm gi

"""
 # *args


# def add(x, y, z, t):
#     return x+y+z+t

# def add(*args): # tap hop cac doi so vi tri ( 1,2,3 ) tra ve tuple
#     print(type(args))
#     return sum(args)

# print(add(1,2,3,4))

# lst = [1, 2, 3, 4]
# # print(*lst) # pha bo ngoac [,] trong loi goi ham

# first, *mid, last = lst # gan tuong ung
# print(first)
# print(mid)
# print(last)

# def add(*lst, operation):
#     return operation(lst)


# print(add(1, 2, 3, 4, operation=min)) # neu operation khong duoc gan ten thi *lst se gom het cac doi so vi tri -> operation se khong co gia tri

def my_func(): # mac dinh tat ca cac ham deu tra ve None
    print("hi")


print(my_func()) # in ra gia tri cua ham mac dinh la None 
"""

"""
 lst = []

a = lst.append(2)  # ham chi thuc hien hanh dong va tra ve None
print(a)  # None

# lst1 = [[]] * 5 # ban dau tao ra 1 list xong nhan 5 tao ra 5 list tham chieu khi thay doi list bd se tro den cac list tao ra
# khac phuc : han che nhan 1 list voi 1 so
lst2 = [[] for _ in range(5)]

lst2[1].append(2)

print(lst2) # [[]*5] 
"""
# doi so mac dinh luon de o phia sau def my_func(a,b=2) b=2 doi so mac dinh