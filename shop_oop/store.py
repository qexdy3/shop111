import json
from product import Product
from user import User
from admin import Admin

class Store:
    def __init__(self):
        self.users = []
        self.products = []
        self.load()

    def load(self):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for u in data["users"]:
                if u["role"] == "admin":
                    user = Admin(u["username"], u["password"])
                else:
                    user = User(u["username"], u["password"])
                    user.history = u["history"]
                self.users.append(user)

            for p in data["products"]:
                self.products.append(Product.from_dict(p))
        except:
            self.users.append(User("user", "123"))
            self.users.append(Admin("admin", "admin"))
            self.products.append(Product(1, "Ноутбук", 70000, "техника"))
            self.products.append(Product(2, "Наушники", 5000, "аксессуары"))
            self.save()

    def save(self):
        data = {
            "users": [],
            "products": []
        }

        for u in self.users:
            data["users"].append({
                "username": u.username,
                "password": u.password,
                "role": "admin" if isinstance(u, Admin) else "user",
                "history": getattr(u, "history", [])
            })

        for p in self.products:
            data["products"].append(p.to_dict())

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def auth(self, login, password):
        for u in self.users:
            if u.username == login and u.password == password:
                return u
        return None
