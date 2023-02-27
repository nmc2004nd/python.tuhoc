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

""" # sum khong cong hon tap
lst = [[1, 2, 3, 4], [10, 29, -10]]  # neu lst[] thi sum=0

total = sum(lst, [1])# list + list
print(total) """

""" lst = ['a', 'b', 'c', 'd']

print(len(lst)) # neu lst trong return 0
print(max(lst)) """

""" # join chi dung voi str neu khong thi phai dung ham map convert

lst = ['4', '3', '2', '1']

s = ''.join(lst)

# s = '-'.join(map(str, lst)) # convert lst thanh str (or ham) ngan cach '-'

print(s) """

""" # bai 1
art_student = {"John", "Max", "Anna", "Bob", "Obito"}
math_student = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
print(art_student.intersection(math_student))  # pt trung gian
print(art_student.difference(math_student))  # pt khac
print(math_student.difference(art_student))  # pt khac
print(art_student.symmetric_difference(math_student))  # all pt tru trung gian
print(art_student.union(math_student))  # all pt """

# bai2
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
# lay value cua key
# print(album_info["album_name"])
# print(album_info["release_year"])
print(album_info.get("album_name"))
print(album_info.get("release_year"))
 #
# album_info["release_year"] = "1971"
# print(album_info["release_year"])

# xoa di phan
# album_info.pop("track_list")
# del album_info["track_list"]

# them key moi

album_info["amount"] = 2000

album_info.update(amount = 2000)
print(json.dumps(album_info, indent=4))

add_album = [("amount",2000)]
album_info.update(add_album)
print(json.dumps(album_info, indent=4))

# lam trong
album_info.clear()
