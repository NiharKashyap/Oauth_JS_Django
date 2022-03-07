#!/bin/sh
source env/scripts/activate
cd oauth_boilerplate
echo "Hello"
python manage.py runsslserver
sleep 2