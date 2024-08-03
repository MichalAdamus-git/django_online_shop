class Order:
    def __init__(self, name, user, product_list:list):
        self.name = name
        self.user = user
        self.product_list = product_list
    def add_product(self, product):
        self.product_list.append(product)