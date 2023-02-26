# list mang nhu c co the chua cac gia tri trung lap
numbers = [1, 2, 3, 4, 1]
#          0  1  2  3  4
#          -5 -4 -3 -2 -1
# print(numbers[0])

# append chen
# numbers.append(100)# chi thuc hien them gia tri vao cuoi list

# remove xoa
# numbers.remove(1)# xoa chu so 1 tim thay dau tien

# pop xoa di gia tri cuoi va gan cho bien
# last_value = numbers.pop()# xoa di gia tri cuoi cung va gan no cho bien khac
# print(last_value)

# extend them vao
# numbers.extend([2,4,6,8]) # them vao list 1 list ms thay doi list ban dau

# numbers[0]=18 # gan gia tri 0

# count dem so lan xuat hien
# amount = numbers.count(1)#dem so lan xuat hien trong list
# print(amount)

# clear xoa list
# numbers.clear()# hoa cac phan tu trong list

# len dem so luong
# amount = len(numbers)# tra ve so luong gia tri trong list
# print(amount)

# insert chen
# numbers.insert(0,18) # chen 18 vao vi tri 0 day cac vi tri le 1
# numbers.insert(1000,18) # vuot qua sl thi chen zo cuoi list
# numbers.insert(-1000,18) # am qua sl thi chen zo dau

# index in ra chi so
# index_of_4 = numbers.index(4) # in ra chi so cua gt trong list
# print(index_of_4)

# reverse
# numbers.reverse() # dao nguoc list

# sort
# numbers.sort() # sap xep list theo thu tu tang dan
# numbers.sort(reverse=True) # sap xep list theo thu tu giam dan

# del [stt] xoa di gia tri trong list

# max tra ve gt lon nhat cung kieu du lieu

# min tra ve gi nho nhat cung kieu du lieu


movies = ["pokemon",
          "doremon",
          "naruto",
          "bakuga"]
add_movie = input("nhap ten bo film: ")
movies.append(add_movie)
print(movies)
print(movies[0])
print(movies[2])
print(movies[-1])
print(len(movies))
# movies.remove("pokemon")
# movies.remove("abc")
# del movies[0]
# del movies[-1]
# print(movies)
# last_movie = movies.pop()
# print(last_movie)
movies.insert(0, "gio")
print(movies)
print(movies.count("One Piece"))
print(movies.index("gio"))
movies.extend(["xxx", "aaa", "uuu"])
print(movies)
movies.clear()
print(movies)
