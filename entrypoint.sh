#!/bin/bash

python create_tables.py --no-input

python from_excel_to_postgres.py --no-input

exec gunicorn --bind 0.0.0.0:5000 wsgi:app
