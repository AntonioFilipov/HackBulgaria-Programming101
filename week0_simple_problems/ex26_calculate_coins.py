coins = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
my_list = [100, 50, 20, 10, 5, 2, 1]


def calculate_coins(sum):
    i = 0
    count = 0
    sum = sum*100

    while(sum != 0):
        if my_list[i] <= sum:
            sum -= my_list[i]
            count += 1
            coins[my_list[i]] = count
        else:
            i += 1
            count = 0
    return (coins)
print(calculate_coins(18.53))

