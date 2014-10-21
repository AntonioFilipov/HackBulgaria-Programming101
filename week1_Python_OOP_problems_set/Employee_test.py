import unittest
from Employee import Employee
from Employee import HourlyEmployee
from Employee import SalariedEmployee
from Employee import Manager


class TestEmployee(unittest.TestCase):
    def test_init(self):
        employee = Employee("Maik")
        self.assertEqual("Maik", employee.name)

    def test_get_name(self):
        employee = Employee("Maik")
        self.assertEqual("Maik", employee.get_name())


class TestHourlyEmployee(unittest.TestCase):
    def test_init(self):
        horly_employee = HourlyEmployee("Brian", 20)
        self.assertEqual("Brian", horly_employee.name)
        self.assertEqual(20, horly_employee.hourly_wage)

    def test_weekly_pay_40_down(self):
        horly_employee = HourlyEmployee("Brian", 20)
        hours = 20
        self.assertEqual(400, horly_employee.weeklyPay(hours))
        hours = 40
        self.assertEqual(800, horly_employee.weeklyPay(hours))

    def test_weekly_pay_40_up(self):
        horly_employee = HourlyEmployee("Brian", 20)
        hours = 41
        self.assertEqual(850, horly_employee.weeklyPay(hours))


class TestSalariedEmployee(unittest.TestCase):

    def test_init(self):
        salaried_employee = SalariedEmployee("Brian", 48000)
        self.assertEqual("Brian", salaried_employee.name)
        self.assertEqual(48000, salaried_employee.salary)

    def test_weekly_pay(self):
        salaried_employee = SalariedEmployee("Brian", 48000)
        self.assertTrue(salaried_employee.weeklyPay(10000))


class TestManager(unittest.TestCase):

    def test_init(self):
        manager = Manager("George", 104000.0, 50.0)
        self.assertEqual("George", manager.name)
        self.assertEqual(50.0, manager.weekly_bonus)

    def weeklyPay(self):
        manager = Manager("George", 48000, 50.0)
        self.assertEqual(10050, manager.weeklyPay(20))


if __name__ == '__main__':
    unittest.main()
