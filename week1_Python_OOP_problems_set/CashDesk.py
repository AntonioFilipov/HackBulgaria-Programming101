class CashDesk():
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money_taken):
        for item in money_taken:
            if money_taken[item] > -1:
                self.money[item] += money_taken[item]
        return self.money

    def total(self):
        sum = 0
        for item in self.money:
            sum += self.money[item]*item
        return sum

    def can_withdraw_money(self, amount_of_money):
        my_list = []
        result = 0

        for item in self.money:
            if self.money[item] > 0 and item <= amount_of_money:
                #print ("self_money.item {}".format(self.money[item]))
                for i in range(0, self.money[item]):
                    my_list.append(item)
        #print (my_list)
        reversed_list = my_list
        reversed_list.sort(reverse=True)
        #print(reversed_list)

        for item in range(0, len(reversed_list)):
            result += reversed_list[item]
            #print (result)
            if result > amount_of_money:
                result -= reversed_list[item]
            elif result == amount_of_money:
                return True
        return False
