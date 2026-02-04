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
