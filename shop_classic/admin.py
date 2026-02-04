def admin_menu(users, products):
    while True:
        print("""
1. Добавить товар
2. Удалить товар
3. Изменить цену
4. Статистика продаж
5. Пользователи
0. Выйти
        """)

        choice = input("Выбор: ")

        if choice == "1":
            try:
                name = input("Название: ")
                price = int(input("Цена: "))
                category = input("Категория: ")

                new_id = products[-1]["id"] + 1
                products.append({
                    "id": new_id,
                    "name": name,
                    "price": price,
                    "category": category,
                    "sold": 0
                })
                print("Товар добавлен")
            except:
                print("Ошибка")

        elif choice == "2":
            try:
                pid = int(input("ID товара: "))
                for p in products:
                    if p["id"] == pid:
                        products.remove(p)
                        print("Товар удалён")
                        break
                else:
                    print("Товар не найден")
            except:
                print("Ошибка")

        elif choice == "3":
            try:
                pid = int(input("ID товара: "))
                for p in products:
                    if p["id"] == pid:
                        p["price"] = int(input("Новая цена: "))
                        print("Цена изменена")
                        break
                else:
                    print("Товар не найден")
            except:
                print("Ошибка")

        elif choice == "4":
            print("\nСтатистика:")
            for p in products:
                print(p["name"], "-", p["sold"])

        elif choice == "5":
            print("\nПользователи:")
            for u in users:
                print(u["username"], "-", u["role"])

        elif choice == "0":
            break

        else:
            print("Неверный пункт")
