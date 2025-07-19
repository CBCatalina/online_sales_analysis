from cart import Cart
import random

# Crează instanța Cart
cart = Cart()

# Adaugă 3 produse selectate aleatoriu în coș
available_products = product_manager.products  # presupunem că product_manager e instanța ProductManager
if len(available_products) < 3:
    print("Nu sunt suficiente produse pentru a adăuga în coș.")
else:
    random_products = random.sample(available_products, 3)
    for product in random_products:
        cart.add_product(product)

# Afișează conținutul coșului și valoarea totală
cart.display_cart()
