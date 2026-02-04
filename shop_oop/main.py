from store import Store
from product import Product
from admin import Admin

store = Store()

print("Интернет-магазин")

while True:
    login = input("Логин: ")
    password = input("Пароль: ")

    user = store.auth(login, password)

    if not user:
        print("Неверные данные")
        continue

    if isinstance(user, Admin):
        while True:
            print("""
1. Добавить товар
2. Удалить товар
3. Статистика
0. Выйти
            """)
            choice = input("Выбор: ")

            if choice == "1":
                name = input("Название: ")
                price = int(input("Цена: "))
                cat = input("Категория: ")
                pid = store.products[-1].id + 1
                user.add_product(store, Product(pid, name, price, cat))
                print("Товар добавлен")

            elif choice == "2":
                pid = int(input("ID: "))
                if user.delete_product(store, pid):
                    print("Удалено")
                else:
                    print("Не найдено")

            elif choice == "3":
                for p in store.products:
                    print(p.name, "-", p.sold)

            elif choice == "0":
                break

    else:
        while True:
            print("""
1. Товары
2. Купить
3. История
4. Сменить пароль
0. Выйти
            """)
            choice = input("Выбор: ")

            if choice == "1":
                for p in store.products:
                    print(p.id, p.name, p.price, p.category)

            elif choice == "2":
                pid = int(input("ID товара: "))
                for p in store.products:
                    if p.id == pid:
                        user.buy(p)
                        store.save()
                        print("Куплено")
                        break

            elif choice == "3":
                for h in user.history:
                    print("-", h)

            elif choice == "4":
                user.change_password(input("Новый пароль: "))
                store.save()

            elif choice == "0":
                break
