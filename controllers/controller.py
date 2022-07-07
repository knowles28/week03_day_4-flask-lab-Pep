import imp
from flask import redirect, render_template, request
from app import app
from models.event import Event
from models.event_list import events, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_description = request.form['description']
    event_room = request.form['room']
    event_guests = request.form['guests']
    new_event = Event(event_date, event_name, event_description, event_room, event_guests)
    add_new_event(new_event)
    print(events)
    return redirect('/events')
    