import logging

my_logger = logging.getLogger()
file_logger = logging.getLogger()
file_logger2 = logging.getLogger()
my_logger.setLevel(logging.INFO)

# create handlers

event_handler = logging.FileHandler('Event.log')
ticket_handler = logging.FileHandler('Ticket.log')
error_handler = logging.FileHandler('Error.log')

# set level for handlers
event_handler.setLevel(logging.INFO)
ticket_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.WARNING)

# create format for handlers
s_format = logging.Formatter('%(levelname)s-%(asctime)s-%(name)s-%(message)s')
event_handler.setFormatter(s_format)
ticket_handler.setFormatter(s_format)
event_handler.setFormatter(s_format)

# add handlers to logger
my_logger.addHandler(event_handler)
file_logger.addHandler(ticket_handler)
file_logger2.addHandler(error_handler)
