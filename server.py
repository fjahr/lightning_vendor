import config
import requests
import json

def new_invoice(amount_mbtc):
    url = config.charge_url + '/invoice'
    amount_msat = int(amount_mbtc*100000000)
    req_data = {'msatoshi': str(amount_msat), 'description': 'lightningvendor.com'}

    r = requests.post(url, data=req_data).json()

    return r['id'], r['payreq']

def invoice_paid(id):
    url = config.charge_url + '/invoice/' + id

    r = requests.get(url).json()

    if r['status'] == 'paid':
        return True
    else:
        return False
