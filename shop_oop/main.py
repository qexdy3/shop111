from store import Store
from product import Product
from admin import Admin

store = Store()

print("=== Интернет-магазин ===")

while True:
    login = input("\nЛогин: ")
    password = input("Пароль: ")

    user = store.auth(login, password)

    if not user:
        print("Неверные данные")
        continue

    print(f"\nДобро пожаловать, {user.username}!")

    if isinstance(user, Admin):
        while True:
            print("""
[АДМИН ПАНЕЛЬ]
1. Добавить товар
2. Удалить товар
3. Изменить цену товара
4. Статистика продаж
5. Список пользователей
0. Выйти
            """)
            choice = input("Выбор → ")

            if choice == "1":
                name = input("Название: ").strip()
                try:
                    price = int(input("Цена: "))
                    cat = input("Категория: ").strip().lower()
                    pid = store.get_next_id()
                    product = Product(pid, name, price, cat)
                    user.add_product(store, product)
                    print(f"Товар '{name}' добавлен (ID: {pid})")
                except ValueError:
                    print("Ошибка: цена должна быть числом")

            elif choice == "2":
                try:
                    pid = int(input("ID товара: "))
                    if user.delete_product(store, pid):
                        print("Товар удалён")
                    else:
                        print("Товар не найден")
                except ValueError:
                    print("Ошибка: ID должен быть числом")

            elif choice == "3":
                try:
                    pid = int(input("ID товара: "))
                    new_price = int(input("Новая цена: "))
                    if user.change_price(store, pid, new_price):
                        print("Цена изменена")
                    else:
                        print("Товар не найден")
                except ValueError:
                    print("Ошибка ввода")

            elif choice == "4":
                print("\nСтатистика продаж:")
                for p in store.products:
                    print(f"  {p.name} — продано {p.sold} шт.")

            elif choice == "5":
                print("\nПользователи:")
                for u in user.list_users(store):
                    role = "Админ" if isinstance(u, Admin) else "Пользователь"
                    print(f"  {u.username} — {role}")

            elif choice == "0":
                break

            else:
                print("Неверный выбор")

    else:  # Обычный пользователь
        while True:
            print("""
[МЕНЮ ПОЛЬЗОВАТЕЛЯ]
1. Показать все товары
2. Сортировать по цене (возр.)
3. Фильтр по категории
4. Добавить в корзину
5. Показать корзину и купить
6. История покупок
7. Сменить пароль
0. Выйти
            """)
            choice = input("Выбор → ")

            if choice == "1":
                print("\nID | Название          | Цена    | Категория")
                print("-" * 50)
                for p in store.products:
                    print(f"{p.id:2} | {p.name:17} | {p.price:7} | {p.category}")

            elif choice == "2":
                sorted_prod = sorted(store.products, key=lambda x: x.price)
                print("\nСортировка по цене (по возрастанию):")
                print("ID | Название          | Цена    | Категория")
                print("-" * 50)
                for p in sorted_prod:
                    print(f"{p.id:2} | {p.name:17} | {p.price:7} | {p.category}")

            elif choice == "3":
                cat = input("Категория: ").strip().lower()
                result = [p for p in store.products if p.category == cat]
                if result:
                    print(f"\nТовары в категории '{cat}':")
                    print("ID | Название          | Цена    | Категория")
                    print("-" * 50)
                    for p in result:
                        print(f"{p.id:2} | {p.name:17} | {p.price:7} | {p.category}")
                else:
                    print("Ничего не найдено")

            elif choice == "4":
                try:
                    pid = int(input("ID товара: "))
                    product = next((p for p in store.products if p.id == pid), None)
                    if product:
                        user.cart.add(product)
                        print(f"Добавлено: {product.name}")
                    else:
                        print("Товар не найден")
                except ValueError:
                    print("Ошибка: ID должен быть числом")

            elif choice == "5":
                if not user.cart.items:
                    print("Корзина пуста")
                    continue

                print("\nВаша корзина:")
                total = 0
                for item, qty in user.cart.to_list():
                    subtotal = item.price * qty
                    total += subtotal
                    print(f"  {qty} × {item.name} — {subtotal} сом")
                print(f"Итого: {total} сом")

                confirm = input("\nОформить покупку? (y/n): ").lower()
                if confirm == "y":
                    success, total = user.checkout()
                    if success:
                        store.save()
                        print(f"Покупка на {total} сом завершена! Спасибо.")
                    else:
                        print("Ошибка при оформлении")

            elif choice == "6":
                if not user.history:
                    print("История пуста")
                else:
                    print("\nИстория покупок:")
                    for i, item in enumerate(user.history, 1):
                        print(f"{i}. {item}")

            elif choice == "7":
                new_pass = input("Новый пароль: ").strip()
                if new_pass:
                    user.change_password(new_pass)
                    store.save()
                    print("Пароль изменён")
                else:
                    print("Пароль не может быть пустым")

            elif choice == "0":
                break

            else:
                print("Неверный выбор")
