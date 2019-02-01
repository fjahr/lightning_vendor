import requests

UPDATE_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

class Price:
    def update_mbtc():
        return update_sat() * 1000

    def update_sat():
        resp = requests.get(UPDATE_URL)
        data = resp.json()

        raw_rate = data['bpi']['EUR']['rate']
        rate = float(raw_rate.replace(',', ''))

        price = 30/(rate*100)

        return price

