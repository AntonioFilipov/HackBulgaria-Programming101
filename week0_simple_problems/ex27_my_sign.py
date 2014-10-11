my_dictionary = {(20, 4): "Aries",
            (21, 5): "Taurus",
            (21, 6): "Gemini",
            (22, 7): "Cancer",
            (22, 8): "Leo",
            (23, 9): "Virgo",
            (23, 10): "Libra",
            (22, 11): "Scorpio",
            (21, 12): "Sagittarius",
            (20, 1): "Capricorn",
            (19, 2): "Aquarius",
            (20, 3): "Pisces"}


def help_month(day, month):
    if month == 1 and day >= 20:
        help_month = 12
        return help_month
    else:
        return month - 1


def what_is_my_sign(day, month):
    
    for item in my_dictionary:
        if item[1] == month:
            if day <= item[0]:
                return (my_dictionary[item])

                


def main():
    print (what_is_my_sign(5, 8))
    print (what_is_my_sign(29, 1))
    print (what_is_my_sign(30, 6))
    print (what_is_my_sign(31, 5))
    print (what_is_my_sign(2, 2))
    print (what_is_my_sign(8, 5))
    print (what_is_my_sign(9, 1))

if __name__ == '__main__':
    main()
