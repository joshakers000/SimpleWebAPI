#! /bin/bash
# A simple script for trying to fix a travis ci issue

./ docker run -i -p 5000:5000 flask-api
./ python3 test.py