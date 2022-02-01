#!/bin/bash
# Sends JSON file via `POST` request to a URL.
curl -sH "Content-Type: application/json" -d "$(cat $2")" "$1"
