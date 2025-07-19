class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product_by_name(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
