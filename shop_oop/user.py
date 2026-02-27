from cart import Cart

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.history = []
        self.cart = Cart()

    def buy(self, product):
        self.cart.add(product)
        product.sold += 1 

    def checkout(self):
        if not self.cart.items:
            return False, 0
        total = self.cart.total()
        for item, qty in self.cart.to_list():
            for _ in range(qty):
                self.history.append(item.name)
        self.cart.clear()
        return True, total

    def change_password(self, new_pass):
        self.password = new_pass
