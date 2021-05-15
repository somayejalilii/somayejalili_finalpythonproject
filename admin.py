import csv
from turtle import pd

from loger import file_logger
from ticket import Ticket


class Admin:
    """
    The class class has been written for the site that the operation of adding ticket and ticket tickets is done in it.
    """

    def __init__(self, name_admin, password_admin, role='admin'):
        self.role = role
        self.name_event = None
        self.exp_event = None
        self.time_event = None
        self.cost_event = None
        self.capacity_event = None
        self.place_event = None
        self.name_admin = name_admin
        self.password_admin = password_admin

    @staticmethod
    def view_event():
        """
        The method for displaying laths is tickets
        """
        event_list = 'list1.csv'
        with open(event_list, 'r') as ticket_csv:
            ticket_r = csv.reader(ticket_csv)
            for row in ticket_r:
                print(row)
        return

    @staticmethod
    def create_event():

        """
        In this method, the admin can add new event to the ticket list
        :return:
        """
        file_list = 'list1.csv'
        id_ticket = input("enter id ticket")
        name_event = input("enter name ticket ")
        expdate_event = input("enter Expiration date")
        time_event = input("enter time ticket")
        cost_event = input("enter cost_ticket")
        capacity_total_event = input("enter capacity total ticket ")
        capacity_residual_event = input("enter capacity residual ticket ")
        place_event = input("enter event place")
        discount_code = input("enter discount_code")
        obj_ticket = Ticket(id_ticket, discount_code, name_event, expdate_event, time_event, cost_event,
                            capacity_total_event,
                            capacity_residual_event, place_event)
        row_dic = [[obj_ticket.id_ticket, obj_ticket.discount_code, obj_ticket.name_event, obj_ticket.expdate_event,
                   obj_ticket.time_event, obj_ticket.cost_event, obj_ticket.capacity_total_event,
                   obj_ticket.capacity_residual_event, obj_ticket.place_event]]
        #row_dic = [int(x.strip()) if x.isdigit() else x for x in row_dic]
        with open(file_list, 'a') as csv_list:
            csv_writer = csv.writer(csv_list)
            csv_writer.writerows(row_dic)
        file_logger.info(f"{row_dic}is created")
        return row_dic

    def __str__(self):
        return
Admin.create_event()


