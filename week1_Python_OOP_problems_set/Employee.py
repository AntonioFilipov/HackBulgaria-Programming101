class Employee():
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def get_name(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        if hours <= 40:
            self.salary = hours*self.hourly_wage
            return self.salary
        else:
            self.salary = hours*self.hourly_wage
            self.salary += (hours - 40)*self.hourly_wage*1.5
            return self.salary


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.salary = annual_salary

    def weeklyPay(self, hours):
        return self.salary / 48


class Manager(SalariedEmployee):
    def __init__(self, name, annual_salary, weekly_bonus):
        super().__init__(name, annual_salary)
        self.weekly_bonus = weekly_bonus

    def weeklyPay(self, hours):
        return self.salary / 48 + self.weekly_bonus

def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))

    for employee in staff:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weeklyPay(hours)
        print("Salary: {}".format(pay))

if __name__ == '__main__':
    main()
