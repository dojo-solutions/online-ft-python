from product import Product
from store import Store

amazon = Store('Amazon')
amazon.add_product(Product('Apple Watch', 450, "Accessories")).add_product(Product('Ray Ban Wayfarers', 100, "Accessories")).add_product(Product('Board Shorts', 50, "Outerwear"))
print(amazon.products)

amazon.inflation(0.02)
print(amazon.products[0].price)

amazon.set_clearance('Accessories', 0.15)
print(amazon.products[1].price)

# sensei bonus check
print(amazon.products[2].id)