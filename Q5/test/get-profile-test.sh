#!/bin/bash

#jamesee6 token
#export ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdG5hbWUiOiJKYW1lcyIsImxhc3RuYW1lIjoiRWUiLCJ1c2VybmFtZSI6ImphbWVzZWU2In0.z5QsElLtoMyK0dvf3okDDwT7DgFfS9NNixQldQACgAQ
#jamesee4 token
ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdG5hbWUiOiJKYW1lcyIsImxhc3RuYW1lIjoiRWUiLCJ1c2VybmFtZSI6IlNHSmFtZXMxIn0.AN1thwssBsFF9G0pVj6-uPE3BG3kbzw_e9Gy8dhsKQE


curl \
--request GET \
--header "authorization: $ACCESS_TOKEN" \
--header 'content-type: application/json' \
--url http://localhost:8000/profile | jq .

