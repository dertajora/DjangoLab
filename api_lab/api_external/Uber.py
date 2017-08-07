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

    # requests.get('https://api.uber.com/v1.2/products?latitude=37.7752315&longitude=-122.418075', headers=headers)
    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # requests.get('https://api.uber.com/v1.2/products?latitude=37.7752315&longitude=-122.418075', headers=headers)

    return data_product