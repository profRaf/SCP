#!/bin/bash
cd /home/ec2-user/Django_Application/virtual_env
. bin/activate
cd ICA-1/ICA
python manage.py runserver 0.0.0.0:8000
