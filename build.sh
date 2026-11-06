#!/usr/bin/env bash
# This script sets up the Django project environment.
set -o errexit


# Install dependencies
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate