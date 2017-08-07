import requests
import json

def get_product_data(token):

    headers = {
        'Authorization': 'Token QBRCerQU0RVas6Ha_Q7cUCkvWAeVALtLuFbEYIid',
        'Accept-Language': 'en_US',
        'Content-Type': 'application/json',
    }

    params = (
        ('latitude', '28.618629'),
        ('longitude', '77.207599'),
    )

    data_product = requests.get('https://api.uber.com/v1.2/products', headers=headers, params=params)

    #  data product from my own API (this API data come from Uber API too)
    data_product = requests.get('https://katakamu.id/barclayseye-api/public/uber/list_product')

    # return bisa menggunakan alternatif berikut
    # http://docs.python-requests.org/en/master/
    # data_product.text
    # data_product.json

    return data_product