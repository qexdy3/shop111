cart = []


def show_products(data):
    print("\nID | Название | Цена | Категория")
    print("-" * 40)
    for p in data:
        print(p["id"], "|", p["name"], "|", p["price"], "|", p["category"])


def user_menu(user, products):
    while True:
        print("""
1. Показать товары
2. Сортировать по цене
3. Фильтр по категории
4. Добавить в корзину
5. Купить
6. История покупок
7. Сменить пароль
0. Выйти
        """)

        choice = input("Выбор: ")

        if choice == "1":
            show_products(products)

        elif choice == "2":
            sorted_products = sorted(products, key=lambda x: x["price"])
            show_products(sorted_products)

        elif choice == "3":
            cat = input("Категория: ").lower()
            result = []
            for p in products:
                if p["category"] == cat:
                    result.append(p)

            if result:
                show_products(result)
            else:
                print("Ничего не найдено")

        elif choice == "4":
            try:
                pid = int(input("ID товара: "))
                for p in products:
                    if p["id"] == pid:
                        cart.append(p)
                        print("Добавлено в корзину")
                        break
                else:
                    print("Товар не найден")
            except:
                print("Ошибка ввода")

        elif choice == "5":
            if not cart:
                print("Корзина пуста")
                continue

            total = 0
            for item in cart:
                total += item["price"]

            print("Сумма:", total)
            confirm = input("Подтвердить покупку? (y/n): ")

            if confirm.lower() == "y":
                for item in cart:
                    user["history"].append(item["name"])
                    item["sold"] += 1
                cart.clear()
                print("Покупка завершена")

        elif choice == "6":
            if not user["history"]:
                print("История пуста")
            else:
                for i in range(len(user["history"])):
                    print(i + 1, "-", user["history"][i])

        elif choice == "7":
            new_pass = input("Новый пароль: ")
            user["password"] = new_pass
            print("Пароль изменён")

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")
