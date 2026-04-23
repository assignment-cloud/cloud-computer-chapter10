#!/bin/bash

# Start the event trigger simulator in the background
echo "Starting Event Trigger Simulator..."
python events/trigger.py &

# Start the Django web server
echo "Starting Django Server..."
gunicorn cloudapp.wsgi --bind 0.0.0.0:$PORT --log-file -
