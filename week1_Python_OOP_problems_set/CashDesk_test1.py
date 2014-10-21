import unittest
from CashDesk import CashDesk


class CashDeskTests(unittest.TestCase):
    def test_take_money(self):
        my_CashDesk = CashDesk()
        self.assertEqual({1: 2, 100: 3, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}, my_CashDesk.take_money({1: 2, 100: 3}))
        self.assertEqual({1: 3, 100: 4, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1}, my_CashDesk.take_money({1: 1, 100: 1, 2: 1, 5: 1, 10: 1, 20: 1, 50: 1}))
        my_CashDesk = CashDesk()
        self.assertEqual({100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}, my_CashDesk.take_money({}))

    def test_take_money_negative(self):
        my_CashDesk = CashDesk()
        self.assertEqual({1: 0, 100: 3, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}, my_CashDesk.take_money({1: -2, 100: 3}))

    def test_total(self):
        my_CashDesk = CashDesk()
        my_CashDesk.take_money({1: 2, 100: 3})
        self.assertEqual(302, my_CashDesk.total())
        my_CashDesk.take_money({1: 2, 100: 3})
        self.assertEqual(604, my_CashDesk.total())
        my_CashDesk.take_money({1: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0})
        self.assertEqual(604, my_CashDesk.total())
        my_CashDesk.take_money({1: 1, 100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1})
        self.assertEqual(792, my_CashDesk.total())

    def can_withdraw_money(self):
        my_CashDesk = CashDesk()
        my_CashDesk.take_money({1: 2, 100: 3})
        self.assertTrue(my_CashDesk.can_withdraw_money(2))
        self.assertTrue(my_CashDesk.can_withdraw_money(302))
        self.assertFalse(my_CashDesk.can_withdraw_money(5))

if __name__ == '__main__':
    unittest.main()
