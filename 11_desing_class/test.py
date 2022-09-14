from Product import Product
from Order import Order

p1 = Product('t-shirt', 12.00)
print(p1)
p2 = Product('pants', 30)
print(p2)
p3 = Product('socks', 2)
print(p3)


products = [p1, p2]
o = Order(products)
o.add_product(p3)
print(o)