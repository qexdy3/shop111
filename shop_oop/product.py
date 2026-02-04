class Product:
    def __init__(self, pid, name, price, category):
        self.id = pid
        self.name = name
        self.price = price
        self.category = category
        self.sold = 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "sold": self.sold
        }

    @staticmethod
    def from_dict(data):
        p = Product(data["id"], data["name"], data["price"], data["category"])
        p.sold = data["sold"]
        return p
