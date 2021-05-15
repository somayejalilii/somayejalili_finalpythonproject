import sys

from admin import Admin
from customer import Customer
from login import register, log_in


def main():
    menu()


def menu():
    print("+++++++++welcome to online sale ticket++++++++++++\n"
          "               1-login:\n"
          "               2-register:\n"
          "               3-exist:\n"
          )
    choice = int(input("please enter your choice :"))
    if choice == 1:
        print("1-admin:\n"
              "2-customer:\n")
        menu1 = int(input("enter your choice :"))
        if menu1 == 1:
            admin_menu()
        elif menu1 == 2:
            customer_menu()
        else:
            menu()
    elif choice == 2:
        register()
    elif choice == 3:
        sys.exit()
    else:
        menu()


def admin_menu():
    log_in()
    print("**********************************************"
          "                1-view list event\n "
          "                2-create event\n "
          "                3-buy ticket\n "
          "                4-Back to previous menu\n ")

    menu_admin = int(input("Enter the desired option :"))
    if menu_admin == 1:
        Admin.view_event()
    elif menu_admin == 2:
        Admin.create_event()
    elif menu_admin == 3:
        Customer.buy_ticket(self=None ,discount_code=None, discount_percent=None, role=None)
    elif menu_admin == 4:
        menu()
    else:
        print("The entered option is not correct!!")
        admin_menu()


def customer_menu():
    log_in()
    print("1-view list event :\n"
          "2-buy ticket :\n"
          "3-Back to previous menu :\n")
    customer_m = int(input("Select the right option :"))
    if customer_m == 1:
        Admin.view_event()
    elif customer_m == 2:
        Customer.buy_ticket(self=None ,discount_code=None, discount_percent=None, role=None)
    elif customer_m == 3:
        menu()
    else:
        print("The entered option is not correct!!")
        customer_menu()


if __name__ == '__main__':
    main()
