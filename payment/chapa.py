import requests
import json
import time

def payment( first, last, phone,amount, email,):
    timestamp = int(time.time())
    url = "https://api.chapa.co/v1/transaction/initialize"
    payload = {
        "amount": amount,
        "currency": "ETB",
        "email": email,
        "first_name": first,
        "last_name": last,
        "phone_number": phone,
        "tx_ref": f"chewatatest-{timestamp}",
        "callback_url": "https://webhook.site/077164d6-29cb-40df-ba29-8a00e59a7e60",
        # "return_url": "https://www.google.com/",
        "customization": {
            "title": "Payment",
            "description": "I love online payments"
        }
    }

    headers = {
        'Authorization': 'Bearer CHASECK_TEST-c9dyz9518rLHBmAERF0mIlNDovNra7Wx',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.text


    return json.loads(data)


# print(payment('kal','amare','0987987444',600,'kalamare@gmail.com'))
