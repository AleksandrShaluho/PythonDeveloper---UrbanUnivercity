class Shop:

    def __init__(self,name):
        self.name = name
        self.__file_name = self.name + '_products.txt'

    def add(self,*products):
        with open(self.__file_name,'+a') as f:
            f.seek(0)
            store = f.read()
            for product in products:
                if product.name in store:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    f.write(f'{product.name}, {product.weight}, {product.category}\n')

    def get_products(self):
        store = open(self.__file_name)
        inventory = store.read()
        store.close()
        return inventory


    def __str__(self):
        return self.name
