"""  if --- elif --- else """
# n = int(input("n= "))
""" a = int(input("a= "))
b = int(input("b= "))
 """
""" if n%3==0:
    print("n chia het cho 3")
else:
    print("n khong chia het cho 3")  """

# print("n chia het cho 3" if n % 3 == 0 else "n khong chia het cho 3") # sort if
""" if a > b:
    print(a)
else:
    print(b)  """
""" m = a
if b > a:
    m=b
print(m)  """

# a, b =2,3 gan tuong ung map tra ve mot day gia tri
""" a, b = map(int, input().split()) """

""" s="a  b c"
print(s.split()) tao thanh list cac phan tu phan cach nhau boi 1 hay nhieu space """

""" print(a if a > b else b) """

# eval danh gia bieu thuc nam trong chuoi vd a=2 print(eval("a"))=2
""" print(eval("1+2 ** 4"))# 17
lst=list(map(eval, input().split()))
print(lst) """

""" lst = [1, 2, 3, 4]

# * pha ngoac in ra 1 2 3 4 && sep = " " ngan cach giua cac ptu
print(*lst, sep=" %") """

# format
x = 2.4567
# print(format(x, ".2f")) #lay sau 2 phan tu va lam tron

# round
# print(round(x))

# pow luy thua

""" # sorted
lst = [4, 3, 2, 10]

new_lst = sorted(lst) # tra ve 1 list hoan toan ms || sort thay doi truc tiep tren list ban dau 

print(new_lst) """

# ord - chr
""" char = "A"

print("ASCII Code:", ord(char)) # return ma ascii cua ki tu """

""" ascii_code = 65
print(chr(ascii_code)) chuyen ma thanh ky tu """

""" # list chuyen str thanh list
s="abcd"
print(list(s))

lst = list(map(eval, input().split()))
print(lst) """

""" # divmod

print(divmod(4, 3))  # 4//3=1 4%3=1

thuong, phan_du = divmod(11, 3)
print(thuong)
print(phan_du) """

""" #bin chuyen nhi phan tra ve mot chuoi
int_number = 10
# binary_string = bin(int_number)
# print(binary_string[2:])
print(format(int_number, "b"))
print(f"{int_number:b}") """