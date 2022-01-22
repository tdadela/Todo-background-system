#!/bin/bash

source venv/bin/activate
export FLASK_DEBUG=1
exec flask run
