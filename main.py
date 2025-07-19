from product_manager import ProductManager
from cart import Cart
import random

pm = ProductManager()

# Adăugăm produse cu nume și cantități noi (modificate față de ce era înainte)
pm.add_product("Minge fotbal", 120, 10)
pm.add_product("Tricou sport", 80, 5)
pm.add_product("Șort alergare", 50, 7)
pm.add_product("Apă minerală", 5, 20)

cart = Cart()

# Verificăm dacă sunt suficiente produse pentru a adăuga în coș
if len(pm.products) < 3:
    print("Nu sunt suficiente produse pentru a adăuga în coș.")
else:
    random_products = random.sample(pm.products, 3)
    for product in random_products:
        cart.add_product(product)

# Afișăm valoarea totală a coșului și produsele din coș
cart.display_cart()
print(f"Total de plată: {cart.calculate_total()} lei")
