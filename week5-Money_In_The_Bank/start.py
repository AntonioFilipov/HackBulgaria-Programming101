import sql_manager
import getpass
import sqlite3
import time


def main_menu(conn, cursor):
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter a username: ")
            password = getpass.getpass(prompt="Enter a password: ")
            while not sql_manager.password_validation(username, password):
                password = getpass.getpass(prompt="Enter a password again: ")
                print("WEAK password")
            sql_manager.register(conn, cursor, username, password)

            print("Registration Successfull")
        elif command == 'login':
            count_wrong_input = 0
            username = input("Enter your username: ")
            password = ""
            while not sql_manager.login(conn, cursor, username, password):
                password = getpass.getpass(prompt="Enter your password: ")
                count_wrong_input += 1
                if count_wrong_input < 5:
                    continue
                else:
                    print("You entered wrong password 5 times!")
                    boom = 30
                    while boom >= 0:
                        time.sleep(1)
                        print("You can enter you password again after:{}sec".format(boom), end='\r')
                        boom -= 1
                    count_wrong_input = 0
            logged_user = sql_manager.login(conn, cursor, username, password)

            if logged_user:
                logged_menu(conn, cursor, logged_user)
            else:
                print("Login failed")
        
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(conn, cursor, logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(conn, cursor, new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(conn, cursor, new_message, logged_user)
        
        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    conn = sqlite3.connect("bank")
    cursor = conn.cursor()
    sql_manager.create_clients_table(conn, cursor)
    main_menu(conn, cursor)

if __name__ == '__main__':
    main()
