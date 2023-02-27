""" Advanced set
    Dictionary: key: value
    sum, len, min, max, join
"""
import json

set1 = {1, 4, 3, 2}
set2 = {2, 3, 10, -10}

""" tim giao hay ptu trung giua hai set(list,tuple) va tra ve 1 set
set3 = set1.intersection(set2)

print(set3)

print(set1 & set2) # & bat buoc phai set """

""" tim phan tu khac trong set1 neu set1 viet truoc
set3 = set1.difference(set2)
print(set3)

print(set1-set2) """

""" # lay ra tat ca cac phan tu trong hai set
set4 = set1.union(set2).union(set3)
print(set4) # alt dat nhieu con tro

print(set1 | set2 | set3) 
"""

""" #lay tat ca cac phan tu tru phan tu trung
set3 = set1.symmetric_difference(set2)
print(set3)

print(set1^set2) """

student = {
    "name": "Bob",
    "age": 23,
    "grades": [45, 67, 90, 98, 99]
}
# print(json.dumps(student, indent=4))

# value = student["age"]  # key de lay value
# value = student.get("id", "SV001")
# print(value)

# student["id"] = "SV001"  # them vao cuoi dictionary
# student["name"] = "Jack" # update value

# student.update(id="SV001", gender="male")

# info = [# list tuple [(,)(,)]
#     ('id', "sv001"),
#     ('gender', "male")
# ]
# student.update(info)

# remove xoa di 1 phan tu

# value = student.pop('name')

# del student["name"]
# print(value)

""" tup = student.popitem() # xoa di cuoi va tra va gia tri do 
print(tup)
print(json.dumps(student, indent=4)) """

""" # keys
# keys = list(student)  # lay ra key
# values = list(student.values())  # lay ra values

# items = list(student.items()) # lay ra tat cac ca key va value
# print(items)
# print(values)
# print(keys)
 """

""" #clear
student.clear()
print(student) """

""" # sum
lst = [[1, 2, 3, 4], [10, 29, -10]]  # neu lst[] thi sum=0

total = sum(lst, [1])# list + list
print(total) """

""" lst = ['a', 'b', 'c', 'd']

print(len(lst)) # neu lst trong return 0
print(max(lst)) """

""" # join chi dung voi str neu khong thi phai dung ham map convert

lst = ['4', '3', '2', '1']

s = ''.join(lst)

# s = '-'.join(map(str, lst)) # convert lst thanh str ngan cach '-'

print(s) """
