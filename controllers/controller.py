import imp
from flask import redirect, render_template, request
from app import app
from models.event import Event
from models.event_list import events, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)