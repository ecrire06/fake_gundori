from django.shortcuts import render
from .models import Currency

data = {}

# ------------------------------------------------------------------------------
# currencyapi

def get_currency():

    import requests
    from requests.structures import CaseInsensitiveDict

    url = "https://api.currencyapi.com/v3/latest"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "clWzSchlvLfYxNdO8YK5I9hH1kRNLCLh3kQ01IG4"

    r = requests.get(url, headers=headers)

    r_json = r.json()

    krw2usd = r_json['data']['KRW']['value']
    jpy2usd = r_json['data']['JPY']['value']
    krw2jpy = round((krw2usd / jpy2usd) * 100, 6)
    last_updated = r_json['meta']['last_updated_at']
    updated_date = last_updated[:10]

    currency_data = {}

    currency_data['krw2usd'] = krw2usd
    currency_data['krw2jpy'] = krw2jpy
    currency_data['last_updated'] = updated_date

#    Currency(krw2usd=krw2usd, krw2jpy=krw2jpy, last_updated=updated_date).save()

    return currency_data

data = {**get_currency()}

# ------------------------------------------------------------------------------

def home(request):
    return render(request, 'index.html', data)