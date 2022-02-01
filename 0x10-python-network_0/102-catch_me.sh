#!/bin/bash
# Cause the server to response with a specific message using `PUT`.
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me 
