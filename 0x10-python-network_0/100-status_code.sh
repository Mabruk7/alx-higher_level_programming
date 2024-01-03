#!/bin/bash 
# script that only shows the response's status code after sending a request to a URL that is supplied as an argument.
curl -s -L -X HEAD -w "%{http_code}" "$1"