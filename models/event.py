class Event():
    
    def __init__(self, date, name, description, room, guests):
        self.date = date
        self.name = name
        self.guests = guests
        self.room = room
        self.description = description
        # self.recurring = recurring ^^ADD TO PARAMETERS
    