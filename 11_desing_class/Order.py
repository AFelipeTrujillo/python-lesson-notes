from Product import Product
class Order:

    count_orders = 0

    def __init__(self, products):
        Order.count_orders += 1
        self._id = Order.count_orders
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)
        return  product

    def total(self):
        total = 0
        for p in self._products:
            total += p.price
        return total

    def __str__(self):
        product_str = ''
        for p in self._products:
            product_str += p.__str__() + '|'
        return f'Order ID: {self._id}\nProducts: {product_str}'

if __name__ == '__main__':
    p1 = Product('t-shirt', 12.00)
    print(p1)
    p2 = Product('pants', 30)
    print(p2)
    products = [p1, p2]
    o = Order(products)
    print(o)