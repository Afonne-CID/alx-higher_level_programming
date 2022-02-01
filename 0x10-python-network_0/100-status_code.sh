#!/bin/bash
# Displays the status code of a GET response
curl -so /dev/null -w "%{http_code}" "$1"
