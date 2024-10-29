class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        return self.name == other.name

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        with open(self.__file_name, 'r') as f:
            return f.read()

    def add(self, *products):
        with open(self.__file_name, 'r') as f:
            existing_products = []
            for line in f:
                a = line.strip().split(', ')
                if a[1]:
                    a1 = Product(a[0], float(a[1]), a[2])
                    existing_products.append(a1)

        with open(self.__file_name, 'a') as f:
            for product in products:
                if product in existing_products:
                    print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
                else:
                    f.write(f'{product.name}, {product.weight}, {product.category}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
