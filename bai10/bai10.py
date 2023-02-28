""" # in ra cac gia tri trong list giu thu tu( set, tuple)
lst = [4, 100, 5, 6]

for value in lst:
    print(value) """

# dict
""" d ={
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
for key in d:
    print(key) # lay ra key
for value in d.values():
    print(value) # lay ra value
for item in d.items():
    print(item) # lay ra key and value tuple
for item in d.items():
    key, value = item
    print(key)
    print(value)
    print("-"*20) """

""" # list comprehensions tao new list
lst = [1, 2, 3, 4]

# new_lst = [2,4,6,8]
new_lst = []

for x in lst:
    value = x*2
    new_lst.append(value)
print(new_lst)    

new_lst = [val * 2 for val in lst]
print(new_lst) """

""" # set comprehensions

set_a = {"a", "b", "c"}

# yeu cau in hoa
new_set = {s.upper() for s in set_a}
print(new_set) """

""" #dict comprehensions
d ={
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

new_d = {
    k: v*2
    for k,v in d.items()
}
print(new_d) """

""" 
+ zip ket hop cac iterator(list set dict) tao ra cac object trong do lai chua cac tuple
+ enumerate 
"""

""" # zip xet theo iterator it pt 

lst1 = ["a", "b", "c"]
lst2 = (1, 2, 3, 4)
lst3 = ["a1", "b1" ]

print(list(zip(lst2, lst1,lst3))) """

# enumerate tao ra cac tuple cung chi so bat dau
""" #       0    1    2
lst = ["a", "b", "c"]

print(list(enumerate(lst,start=1))) """

""" lst1 = ("a", "b", "c")
lst2 = (1, 2, 3)

print(list(zip(lst1,lst2))) # ra cac list [(),()]
print(dict(zip(lst1,lst2))) # ra cac dict {:,:,:} """

""" 
lst = [1, 2, 3]

new_lst=[val**3 for val in lst] # khong truy cap duoc ben ngoai
print(new_lst)

new_lst = []

for x in lst:
    v=x**3
    new_lst.append(v)
print(x)    # in ra x truy cap duoc ben ngoai
print(new_lst)   """

""" numbers = [100, 34, 56, 78, 80, -46, 3, 5, -11]

# new_lst = [x for x in numbers if x % 2 != 0]
# print(new_lst)
# print(sum(new_lst))

new_lst = [x*2 if x % 2 == 0 else x*3 for x in numbers]
print(new_lst)

new_lst = []
for x in numbers:
    if(x%2==0):
        new_lst.append(x*2)
    else:
        new_lst.append(x*3)
print(new_lst)            
 """

# zip
# enumerate -> ()()()

lst = [1, 2, 3]

""" print(list(enumerate(lst,start=1)))

for idx, value  in enumerate(lst,start=1):
    print(f"{idx}- {value}") """

# print(list(zip(enumerate(lst,start=1)))) # chi 1 phan tu nen khong the gan tuong duong idz and value

""" for i in range(len(lst)):
    if i % 2 !=0:
        print(i,lst[i]) """

for i, v in enumerate(lst):
    if i % 2 != 0:
        print(i, v)
