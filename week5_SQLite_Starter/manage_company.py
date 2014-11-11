import sqlite3


def list_employees(cursor):
    result = cursor.execute("SELECT id, name, possition FROM users")
    for row in result:
        print ("{}.{} - {}".format(row['id'], row['name'], row['possition']))


def monthly_spending(cursor):
    count_sum = 0
    result = cursor.execute("SELECT monthly_salary FROM users")
    for row in result:
        count_sum += row['monthly_salary']
    return count_sum


def yarly_spending(cursor):
    count_sum = 0
    result = cursor.execute("SELECT yearly_bonus FROM users")
    for row in result:
        count_sum += row['yearly_bonus']
    count_sum = count_sum + monthly_spending(cursor)*12
    return count_sum


def add_employee(cursor, db):
    name = input("Enter a name:")
    salary = input("Enter a salary:")
    bonus = input("Enter a yearly bonus:")
    possition = input("Enter a possition:")
    cursor.execute('''
    INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                        VALUES(?,?,?,?)''', (name, salary, bonus, possition))
    db.commit()


def delete_employee(id_number, cursor, db):
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (id_number,))
    db.commit()


def update_employee(id_number, cursor, db):
    name = input("Enter a name:")
    salary = input("Enter a salary:")
    bonus = input("Enter a yearly bonus:")
    possition = input("Enter a possition:")
    cursor.execute('''UPDATE users SET name = ?,
                                        monthly_salary = ?,
                                        yearly_bonus = ?,
                                        possition = ? WHERE id = ? ''', (name, salary, bonus, possition, id_number))
    db.commit()



def main():
    db = sqlite3.connect('mydb')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    print("=======================================================================================================")
    print("Commands are:")
    print("list_employees - list of all employees in the company")
    print("monthly_spending - prints out the total sum of mounthly spending for salaries")
    print("yearly_spending - prints out the total sum of one year of operation")
    print("add_employee - the program starts to promt for data, to create a new employee")
    print("delete_employee <employee_id> - the program should delete the given employee from the database")
    print("update_employee <employee_id> - the program should prompt the user to change each of the fields for the given employee ")
    print("exit - exit the program")
    print("=======================================================================================================")

    while (True):
        command = input("Enter a command:")
        commands = command.split()
        if commands[0] == "list_employees":
            list_employees(cursor)
        elif commands[0] == "monthly_spending":
            print ("The company is spending ${} every mounth!".format(monthly_spending(cursor)))
        elif commands[0] == "yearly_spending":
            print ("The company is spending ${} every year!".format(yarly_spending(cursor)))
        elif commands[0] == "add_employee":
            add_employee(cursor, db)
        elif commands[0] == "delete_employee":
            delete_employee(commands[1], cursor, db)
        elif commands[0] == "update_employee":
            update_employee(commands[1], cursor, db)
        elif commands[0] == "exit":
            break
        else:
            print ("No such command")
if __name__ == '__main__':
    main()