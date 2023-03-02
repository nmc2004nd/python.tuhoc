import random
print("Chào mừng bạn đến với thế giới của những con số!")
print()
print("Hôm nay bạn có thấy con số nào thú vị không!")
print()
print("Hãy đưa ra lựa chọn của bạn: ")
print()
your_choice = int(input("Con số bạn nghĩ đến là: "))
print()
result = random.randint(1, 100)
solanmax = 5
while your_choice != result:
    solanmax -= 1
    print("Rất tiếc, con số bạn chọn chưa chính xác rồi!")
    print()
    print("Thử lại lần nữa nào!")
    print()
    print(f"Bạn còn {solanmax} lần chọn")
    print()
    if solanmax == 0:
        break
    your_choice = int(input("Con số bạn nghĩ đến là: "))
    print()
    if your_choice == result:
        print("Chúc mừng bạn đã đoán đúng!")
        print()
        print(f"Con số may mắn của ngày hôm nay là: {result}")
        print()
        print("Hẹn gặp lại bạn lần sau!")
        break
if your_choice == result and solanmax == 5:
    print("Chúc mừng bạn đã đoán đúng!")
    print()
    print(f"Con số may mắn của ngày hôm nay là: {result}")
    print()
    print("Hẹn gặp lại bạn lần sau!")
if solanmax == 0 and your_choice != result:
    print("Bạn đã hết quyền lựa chon")
    print()
    print("Trò chơi đã kết thúc!")
    print()
    print(f"Con số may mắn của ngày hôm nay là: {result}")
    print()
    print("Chúc bạn may mắn lần sau!")
    print()
