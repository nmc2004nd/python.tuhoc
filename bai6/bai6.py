""" Set khong chua cac gia tri trung lap

tuple """

""" tuple khong the thay doi gia tri trong no """

from copy import deepcopy # copy nguyen bd khong thay doi sau
tup1 = 1, 2, 3
tup2 = (1, 2, 3)
tup3 = 1,
tup4 = (1,)
# print(tup1[-1]) # truy cap phan tu giong list

# not append not change value

# tup1 += (4, 5, 6) chen them pt cho tuple
# print(tup1)

""" set so sanh hai hay nhieu tap hop && khong thu truy cap bang chi so """

set1 = set()  # set trong

set1.add(1)  # them 1 phan tu zo set chi chen 1 lan neu chua co

set1.update([2, 3, 4, 5])  # cap nhat phan tu trong set

set1.remove(1)  # xoa phan tu trong set

set2 = set1.copy()  # copy

set1.clear()  # trong phan tu
# print(set1 is set2)#false khac id
# print(set1 == set2)#true noi dung

set3 = {1, 2, 3, 4}

set6 = {}  # dir

set3.add("kenny")  # add duoc khi them vao khong thay doi duoc
# print(type(set3))
# print(set3)
set4 = {1, 2, 3, 4}
print(set4.pop())  # lay ra ngau nhien 1 gia tri va xoa ik trong set

# tao moi truong ao cong viec lien quan den thu vien
# terminal python -m venv venv
# ctrl j
# pip install pandas
# pip freeze kiem tra cac thu vien
# pip freeze > requirements.txt tao file hien thi pip

""" cu phap tuong ung
t = 4, 5
a, b = t a = 4, b = 5 """

""" 
list tuple

friends=[
    (a,18)
    (b,19)
    (c,20)
] """
#           0          1
#       0     1
#           0  1     0  1
""" lst = [[1, [2, 3]], (4, 5)]
lst_1 = lst.copy()  # copy dau[] noi dung thay doi se duoc cap nhat
lst_1 = lst[:]
lst1 = deepcopy(lst)

lst[0][1].append(100)
print(lst1) """


# kiem tr kieu du lieu
print(isinstance(True, int))  # tra ve True khi thuoc dung kieu du lieu
# bool(int) ke thua

# ma hoa 1 ky tu duy nhat ra ma ^ XOR mach logic: 0^0=0, 1^1=0, 1^0=1
print(ord('1') ^ ord('3'))

print(abs(-True))  # khong dung cho str
print(abs(1+2j))  # modun cua so phuc

print(repr("a"))  # in ra dau nhay ''

s = "a"
a=3
print(f"{s!r}")
print(f"{a!r}")
