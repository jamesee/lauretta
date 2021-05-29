#!/bin/bash

DATA='{"username": "SGJames1","firstname": "James","lastname" : "Ee","password" : "helloworld"}'
echo "REGISTER_DATA=$DATA"



curl \
--request POST \
--data "$DATA" \
--header 'content-type: application/json' \
--url http://localhost:8000/register | jq .
