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
