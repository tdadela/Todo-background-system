#!/bin/bash

echo 'Creating virtual environment.'
python3 -m venv venv || { echo 'Creating virtual environment failed.' ; exit 1; }
source venv/bin/activate || { echo 'Activating virtual environment failed.' ; exit 1; }

echo 'Python libraries installation.'
pip3 install -r requirements.txt

echo 'Creating .flaskenv file'
touch .flaskenv
echo 'FLASK_APP=website.py' >> .flaskenv

echo 'To run the website with debug mode on: ./run_gui.sh'
echo 'To run the website as desktop app: source venv/bin/activate && python gui.py'
