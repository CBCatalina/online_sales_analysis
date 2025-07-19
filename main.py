from product import Product
from product_manager import ProductManager

# Instanțiere manager
manager = ProductManager()

# Adăugare produse
manager.add_product(Product("Tricou sport", 99.99, 10))
manager.add_product(Product("Pantaloni trening", 149.99, 5))
manager.add_product(Product("Adidași alergare", 299.99, 3))

# Afișare produse
manager.display_products()

# Valoare totală inventar
print(f"Valoarea totală a inventarului: {manager.total_value()} lei")
