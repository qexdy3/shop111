from user import User

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_product(self, store, product):
        store.products.append(product)
        store.save()

    def delete_product(self, store, pid):
        for p in store.products:
            if p.id == pid:
                store.products.remove(p)
                store.save()
                return True
        return False

    def change_price(self, store, pid, new_price):
        for p in store.products:
            if p.id == pid:
                p.price = new_price
                store.save()
                return True
        return False

    def list_users(self, store):
        return store.users
        
    def show_products_list(self, store):
        if not store.products:
            print("Список товаров пуст.")
            return

        print("\n" + "="*60)
        print("Список всех товаров:")
        print("ID | Название              | Цена     | Категория     | Продано")
        print("-"*60)

        for p in sorted(store.products, key=lambda x: x.id):
            name = p.name[:20] + "..." if len(p.name) > 20 else p.name.ljust(20)
            category = p.category[:13] + "..." if len(p.category) > 13 else p.category.ljust(13)
            print(f"{p.id:2} | {name} | {p.price:8} | {category} | {p.sold:6}")

        print("="*60)
