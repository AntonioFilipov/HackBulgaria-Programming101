class Product():
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price

    def print_func(self):
        print ("{} {} {}".format(self.name, self.stock_price, self.final_price))


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM

    def print_func(self):
        print ("{} {} {} {} {}".format(self.name, self.stock_price, self.final_price, self.diskspace, self.RAM))


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels

    def print_func(self):
        print ("{} {} {} {} {}".format(self.name, self.stock_price, self.final_price, self.display_size, self.mega_pixels))


class Store():
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.profit = 0

    def print_func(self):
        print ("{} {}".format(self.name, self.products))

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
            return self.products[product]
        else:
            self.products[product] = count
            return self.products[product]

    def list_products(self, product_class=object):
        for item in self.products:
            if isinstance(item, product_class):
                #print ("{} - {}".format(item.name, self.products[item]))
                return("{} - {}".format(item.name, self.products[item]))

    def sell_product(self, product):
        if product in self.products and self.products[product] > 0:
            self.products[product] -= 1
            self.profit += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.profit
