#!/bin/bash

# URL to send requests to

# Send 5 requests to the URL
for i in {1..100}
do
   curl -X 'POST' \
  'http://0.0.0.0:5000/insertMerchant' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'pinCode='$i'&merchID='$i
done
