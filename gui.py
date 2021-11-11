#!/usr/bin/python
'''Run flask web app as desktop app.'''
from flaskwebgui import FlaskUI
from app import app

# app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500)

if __name__ == "__main__":
    # app.run() for debug
    ui.run()
