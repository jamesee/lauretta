#!/bin/bash

curl \
--request POST \
--data '{"username": "SGJames1","password" : "helloworld"}' \
--header 'content-type: application/json' \
--url http://localhost:8000/login | jq '.token' 

