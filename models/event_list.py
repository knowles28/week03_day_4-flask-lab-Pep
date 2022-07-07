from models.event import *

event1 = Event("monday","football", 50, "Room A", "Euro 2020 final")
event2 = Event("tuesday", "tennis", 30, "Room B", "Roland Garros")
event3 = Event("wednesday", "rugby", 20, "Room C", "Six Nations")
event4 = Event("thursday", "golf", 10, "Room D", "The Open")
event5 = Event("friday", "cricket", 5, "Room E", "The Ashes")

events = [event1, event2, event3, event4, event5]

def add_new_event(event):
    events.append(event)
