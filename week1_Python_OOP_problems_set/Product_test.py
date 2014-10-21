import unittest
from Product import Product
from Product import Laptop
from Product import Smartphone
from Product import Store


class TestProduct(unittest.TestCase):
    def test_profit(self):
        my_product = Product("Laptop", 1000, 1200)
        self.assertEqual(200, my_product.profit())


class TestLaptop(unittest.TestCase):
    def test_init(self):
        my_laptop = Laptop("Lenovo", 1000, 1200, 500, 4)
        self.assertEqual("Lenovo", my_laptop.name)
        self.assertEqual(1000, my_laptop.stock_price)
        self.assertEqual(1200, my_laptop.final_price)
        self.assertEqual(500, my_laptop.diskspace)
        self.assertEqual(4, my_laptop.RAM)


class TestSmartphone(unittest.TestCase):
    def test_init(self):
        my_smartphone = Smartphone("Nokia", 1000, 1200, 4, 12)
        self.assertEqual("Nokia", my_smartphone.name)
        self.assertEqual(1000, my_smartphone.stock_price)
        self.assertEqual(1200, my_smartphone.final_price)
        self.assertEqual(4, my_smartphone.display_size)
        self.assertEqual(12, my_smartphone.mega_pixels)


class TestStore(unittest.TestCase):
    def test_load_new_products_empty(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        self.assertEqual(20, my_store.load_new_products(new_laptop, 20))

    def test_load_new_product(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        my_store.load_new_products(new_laptop, 20)
        self.assertEqual(40, my_store.load_new_products(new_laptop, 20))

    def test_list_product(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        my_store.load_new_products(new_laptop, 20)
        self.assertEqual("HP HackBook - 20", my_store.list_products(Laptop))

    def test_sell_product_true(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        my_store.load_new_products(new_laptop, 20)
        self.assertTrue(my_store.sell_product(new_laptop))

    def test_sell_product_false(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        my_store.load_new_products(new_laptop, 0)
        self.assertFalse(my_store.sell_product(new_laptop))

    def test_total_income(self):
        my_store = Store("Ardes")
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        my_store.load_new_products(new_laptop, 20)
        my_store.sell_product(new_laptop)
        self.assertEqual(243, my_store.total_income())
if __name__ == '__main__':
    unittest.main()
