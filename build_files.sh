#!/bin/bash
# Activate Vercel's default Python environment
python3.9 -m venv venv
source venv/bin/activate

# Install requirements
venv/bin/pip install -r requirements.txt

# Collect static files
venv/bin/python3.9 manage.py collectstatic --noinput
