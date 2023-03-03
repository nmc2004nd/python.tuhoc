USER_MENU = """ Nhập 
a - Thêm một bộ phim mới
l - Thông tin của bộ phim
s - Tìm kiếm phim theo tên
x - Xoá phim theo tên
u - Cập nhật thông tin
q - thoát
Lựa chọn của bạn là:  """

movies = []
prves = set()

def add_movie():
    name        = input("Nhập vào tên bộ phim: ")
    while name in prves:
        print("Bộ phim đã tồn tại, vui lòng nhập lại!")
        name    = input("Nhập vào tên bộ phim: ")
    director    = input("Nhập vào tên nhà sản xuất: ") 
    release     = input("Nhập vào năm phát hành: ") 

    movie = {
        "name":           name,
        "director":       director,
        "release":        release
    }  

    movies.append(movie)
    prves.add(name)

def show_movie(movie):
    movie_name          = movie["name"]  
    movie_director      = movie["director"]
    movie_release       = movie["release"]

    print(f"Tên bộ phim\t\t: {movie_name}")
    print(f"Nhà sản xuất\t: {movie_director}")
    print(f"Năm phát hành\t: {movie_release}")

def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print("Thông tin bộ phim:",idx)
            show_movie(movie)
    else:
        print("Danh sách phim trống!")

def search_movie():
    if movies:
        name                = input("Nhập vào tên bộ phim: ")
        for idx, movie in enumerate(movies, start=1):
            if name == movie["name"]:
                print("Thông tin bộ phim:",idx)
                show_movie(movie)
                break
            else:
                print("Không tìm thấy bộ phim",name)
    else:
        print("Danh sách phim trống!")

def remove_movie():
    if movies:
        name                = input("Nhập vào tên bộ phim: ")
        for idx, movie in enumerate(movies):
            if name == movie["name"]:
                del movies[idx]
                print("Xoá thành công")
                break
            else:
                print("Không tìm thấy bộ phim",name)
    else:
        print("Danh sách phim trống!")

def update_movie(): 
    if movies:
        name                = input("Nhập vào tên bộ phim: ")
        founds = [
            idx
            for idx, movie in enumerate(movies)
            if name == movie["name"]
        ]
        if founds:
            position                = founds[0]
            movies[position]["director"]            = input("Nhập vào tên nhà sản xuất: ")
            movies[position]["release"]             = input("Nhập vào năm phát hành: ")
            print("Cập nhật thành công")
        else:
            print("Không tìm thấy bộ phim có tên",name)    
    else:
        print("Danh sách phim trống!")       

option = {
    "a":    add_movie,
    "l":    show_movies,
    "s":    search_movie,
    "x":    remove_movie,
    "u":    update_movie
}

while 1 :
    user_choice = input(USER_MENU)
    if user_choice in option:
        operation   = option[user_choice]
        operation()
    elif user_choice == "q":
        break
    else:
        print("Nhập vào không hợp lệ, yêu cầu nhập lại!")    