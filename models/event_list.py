from models.event import *

event1 = Event("2022-07-01","football", "Euro 2020 final", "Room A", 50)
event2 = Event("2022-07-02", "tennis", "Roland Garros", "Room B", 30)
event3 = Event("2022-07-04", "rugby", "Six Nations", "Room C", 20)
event4 = Event("2022-07-03", "golf", "The Open", "Room D", 10)
event5 = Event("2022-0703", "cricket", "The Ashes", "Room E", 5)

events = [event1, event2, event3, event4, event5]

def add_new_event(event):
    events.append(event)
