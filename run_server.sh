#!/bin/bash
sleep 20
gunicorn --workers=2 -b 0.0.0.0:8000 server:app