import base64
import requests
import keys
from requests.auth import HTTPBasicAuth
from datetime import datetime

unformated_time = datetime.now()
formatted_time = unformated_time.strftime("%Y%m%d%H%M%S")

data_to_encode = keys.business_shortcode + \
    keys.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print(r.json())

json_response = r.json()

my_access_token = json_response['access_token']


def lipa_na_mpesa():

    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortcode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": " 123456787",
        "TransactionDesc": "Pay chaguo lako"
    }

    response = requests.post(api_url, json=request, headers=headers)


lipa_na_mpesa()
