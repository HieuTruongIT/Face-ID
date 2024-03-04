from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['FaceID']
collection = db['users']

username = input("Nhập tên: ")
email = input("Nhập email: ")
password = input("Nhập mật khẩu: ")

user_data = {
    "username": username,
    "email": email,
    "password": password
}

result = collection.insert_one(user_data)

if result.inserted_id:
    print("Người dùng được thêm vào thành công.")
else:
    print("Có lỗi khi thêm người dùng.")
