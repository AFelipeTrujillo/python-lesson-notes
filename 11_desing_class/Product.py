class Product:
    count_products = 0

    def __init__(self, name, price):
        Product.count_products += 1
        self._id = Product.count_products
        self._name = name
        self._price = price

    @property
    def price(self):
        return  self._price

    def __str__(self):
        return f'Id {self._id} {self._name} {self._price}'

if __name__ == '__main__':
    p1 = Product('t-shirt',12.00)
    print(p1)
    p2 = Product('pants', 30)
    print(p2)
