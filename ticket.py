class Ticket:
    """
    In this class, the possibility of purchasing tickets and calculating the price is done with the discount and edit
    list of tickets listings
    """

    def __init__(self, id_ticket, discount_code, name_event, expdate_event, time_event, cost_event,
                 capacity_residual_event, capacity_total_event, place_event):
        self.id_ticket = id_ticket
        self.discount_code = discount_code
        self.name_event = name_event
        self.expdate_event = expdate_event
        self.time_event = time_event
        self.capacity_total_event = capacity_total_event
        self.capacity_residual_event = capacity_residual_event
        self.place_event = place_event
        self.cost_event = cost_event
