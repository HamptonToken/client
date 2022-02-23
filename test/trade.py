import json
import base64
import requests
import time
import hmac
import hashlib


api_key = '' #put here your public key
secret_key = '' #put here your secret key
request = '/api/v4/trade-account/balance' #put here request path. For obtaining trading balance use: /api/v4/trade-account/balance
baseUrl = 'https://whitebit.com' #domain without last slash. Do not use https://whitebit.com/
#If the nonce is similar to or lower than the previous request number, you will receive the 'too many requests' error message
nonce = str(int(time.time())) #nonce is a number that is always higher than the previous request number


data = {
  'ticker': 'HMETA', #for example for obtaining trading balance for HMETA currency
  'request': request,
  'nonce': nonce
}

#preparing request URL
completeUrl = baseUrl + request

data_json = json.dumps(data, separators=(',', ':')) #use separators param for deleting spaces
payload = base64.b64encode(data_json.encode('ascii'))
signature = hmac.new(secret_key.encode('ascii'), payload, hashlib.sha512).hexdigest()

#preparing headers
headers = {
    'Content-type': 'application/json',
    'X-TXC-APIKEY': api_key,
    'X-TXC-PAYLOAD': payload,
    'X-TXC-SIGNATURE': signature,
}

#sending request
resp = requests.post(completeUrl, headers=headers, data=data_json)

#receiving data
print(json.dumps(resp.json(), sort_keys=True, indent=4))
