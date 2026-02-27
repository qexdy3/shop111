class Cart:
    def __init__(self):
        self.items = []  

    def add(self, product):
        for item in self.items:
            if item["product"].id == product.id:
                item["quantity"] += 1
                return
        self.items.append({"product": product, "quantity": 1})

    def remove(self, product_id):
        self.items = [item for item in self.items if item["product"].id != product_id]

    def clear(self):
        self.items = []

    def total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def to_list(self):
        return [(item["product"], item["quantity"]) for item in self.items]
