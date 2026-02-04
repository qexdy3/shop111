class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.history = []

    def buy(self, product):
        self.history.append(product.name)
        product.sold += 1

    def change_password(self, new_pass):
        self.password = new_pass
