for i in {1..10}; do
        curl -X 'POST' 'http://0.0.0.0:5000/insertMerchant' -H 'accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d "pinCode=$i&merchID=$i" &
        curl -X 'POST' 'http://0.0.0.0:5000/getMerchants' -H 'accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d "pinCode=$i" &
done

wait
