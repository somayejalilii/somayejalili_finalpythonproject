import csv
import sys
import pandas as pd
from loger import file_logger2, my_logger
from colorama import Fore

class Customer:
    def __init__(self, name, password, discount_code, discount_percent, role):
        """
        Client class has name and password features of
        discount code and customer nature
        :param name:
        :param password:
        :param discount_code:
        :param role:
        """
        self.name = name
        self.password = password
        self.discount_cod = discount_code
        self.discount_percent = discount_percent
        self.role = role

    @staticmethod
    def buy_ticket():
        """
        In this method, the ticket code and number of users are received from the user and,
         if having a discount code,
          is calculated with a discount percentage,
            and otherwise the price is calculated without discounts.
             The CSV file is updated after each purchase

        """
        try:
            file_list = "list1.csv"
            location = 0
            row_n = input("To purchase tickets, enter the purchase code ")
            number_ticket = int(input("number ticket : "))
            change = pd.read_csv('list1.csv')
            with open(file_list, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if int(row['capacity_residual_event']) >= int(number_ticket):
                        change_capacity = int(row['capacity_residual_event']) - int(number_ticket)
                        change.loc[location, 'capacity_residual_event'] = change_capacity
                        change.to_csv('list1.csv', index=False)
                        file_logger2.info("update file")
                    else:
                        print(Fore.RED+"The number entered is more than the ticket capacity ")
                        sys.exit()
                    location += 1
        except Exception as e:
            print(str(e))
            sys.exit()
        try:
            cod = input(Fore.BLUE+"If you have a discount code, 1 and otherwise, enter the number 2 :")
            if cod == "1":
                dis_cod = int(input("If you have a discount code, enter it : "))
                try:
                    with open('role.csv', 'r+') as event_file:
                        csv_reader = csv.DictReader(event_file)
                        for row in csv_reader:
                            if dis_cod == int(row["discount_code"]):
                                with open('list1.csv', 'r') as event_csv2:
                                    csv_reader1 = csv.DictReader(event_csv2)
                                    for roww in csv_reader1:
                                        print(roww.keys())
                                        if row_n == roww["id_ticket"]:
                                            cost = int(roww["cost_event"])* number_ticket -((int(roww["cost_event"]) * number_ticket) * int(row["discount_percent"]) / 100)
                                            print(Fore.GREEN+f"                   ---------------------Latacia {cost} Deposit----------------------------")
                                            return
                            # else:
                            #     print("The entered code is not correct")
                except Exception as d:
                    print(d)
                    sys.exit()
            elif cod == "2":
                with open('list1.csv', 'r') as event_csv:
                    csv_read = csv.DictReader(event_csv)
                    for ticket_row in csv_read:
                        print(ticket_row.keys())
                        if row_n == ticket_row["id_ticket"]:
                            cost = int(ticket_row["cost_event"]) * number_ticket
                            print(cost)
                            print(Fore.GREEN+"                      --------------------------------------Latacia", cost, "Deposit-------------------------------")
                        else:
                            print(row_n, row["id"])
            my_logger.warning(f"{row_n}is created")
        except Exception as n:
            print(n)
            sys.exit()

    def __str__(self):
        return

