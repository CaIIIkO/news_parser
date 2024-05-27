#!/bin/sh
gunicorn --workers=1 -b=0.0.0.0:8080 news_server.wsgi:application