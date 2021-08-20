#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed
curl -s "$1" -H "content-type: application/json" -d @"$2"
