#!/bin/bash

# test http://localhost:8000/register api
echo ""; echo "====================================================================="
REGISTER_DATA='{"username": "sgjamesee18","firstname": "James","lastname" : "Ee","password" : "helloworld"}'
URI=http://localhost:8000/register 

echo "REGISTER_DATA=$REGISTER_DATA"
echo "URI=$URI"

curl \
--request POST \
--data "$REGISTER_DATA" \
--header 'content-type: application/json' \
--url "$URI" | jq .



# test login api
echo ""; echo "====================================================================="
LOGIN_DATA=$(echo "$REGISTER_DATA" | jq '{username: .username, password: .password}')
URI=http://localhost:8000/login

echo "LOGIN_DATA=$LOGIN_DATA"

curl \
--request POST \
--data "$LOGIN_DATA" \
--header 'content-type: application/json' \
--url "$URI" | jq '.token' 



# test profile api
echo ""; echo "====================================================================="
export ACCESS_TOKEN=$(
curl \
--request POST \
--data "$LOGIN_DATA" \
--header 'content-type: application/json' \
--url "$URI" | jq '.token' | sed 's/\"//g' 
)

echo "ACCESS_TOKEN=$ACCESS_TOKEN"
URI=http://localhost:8000/profile

curl  \
--request GET \
--header "authorization: $ACCESS_TOKEN" \
--header 'content-type: application/json' \
--url "$URI" | jq . 