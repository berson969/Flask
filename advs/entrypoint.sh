#!/bin/sh

gunicorn main:adv -b 0.0.0.0:5001 --forwarded-allow-ips="*" --capture-output --access-logfile error.log

#--forwarded-allow-ips="*"