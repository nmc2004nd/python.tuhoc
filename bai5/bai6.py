""" list in list
copy list
list slicing """
#                0         1
#             0    1      0     1
""" friends = [["ly", 19], ["duc", 18]]
print(friends[0][0]) #in ra ly
 """

# copy
""" lst1 = [1, 2, 3]
lst2 =lst1.copy() """
# is vi tri bo nho id : dia chi bo nho
""" print(lst1 is lst2)# khac vi lst2 copy cua lst1 vd nhu photo cung noi dung khac to giay
print(lst1 == lst2)
print(id(lst1)) hien id
 """
# list slicing => new list lay ra va tao a[start:stop:step] khong lay gia tri stop
""" a = [1, 3, 5, 7, 9]
new_list = a[::-1] in nguoc list
new_list = a[0:2:1] bat dau tu khong va ket thuc o 2 nhung khong lay o 2 buoc nhay mac dinh la 1
print(new_list) """
# b= [-5,256] thuoc khoang nay gt da duoc tao san ngoai khoang phai tao gt
# b = 257 int(257) toa ra int(257) xong tao bien b bien b tro den int(257)

""" friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
print(friends[0:4])
print(friends[3:])
print(friends[0:])
print(friends[::-1])
new_friends = friends.copy()
print(new_friends)
print(friends[1:]) """

""" students = [["SV001", "Bob", "23"], [
    "SV002", "Kenny", "34"], ["SV003", "Henry", "45"]]
print(f"ID:{students[0][0]}, name:{students[0][1]}, age:{students[0][2]}")
print(f"tuoi SV002:{students[1][2]}")
print(students[1:])
print(f"Id:{students[2][0]}") """
