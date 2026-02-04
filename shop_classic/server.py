from user import user_menu
from admin import admin_menu

users = [
    {
        "username": "user",
        "password": "123",
        "role": "user",
        "history": []
    },
    {
        "username": "admin",
        "password": "admin",
        "role": "admin"
    }
]

products = [
    {"id": 1, "name": "Ноутбук", "price": 70000, "category": "техника", "sold": 0},
    {"id": 2, "name": "Наушники", "price": 5000, "category": "аксессуары", "sold": 0},
    {"id": 3, "name": "Смартфон", "price": 45000, "category": "техника", "sold": 0}
]


def auth():
    login = input("Логин: ")
    password = input("Пароль: ")

    for user in users:
        if user["username"] == login and user["password"] == password:
            return user

    print("Неверный логин или пароль")
    return None


print("Добро пожаловать в интернет-магазин")

while True:
    current_user = auth()
    if current_user:
        if current_user["role"] == "user":
            user_menu(current_user, products)
        else:
            admin_menu(users, products)
