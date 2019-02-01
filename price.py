import requests

UPDATE_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

class Price:
    def update_mbtc(self):
        return self.update_sat() * 1000

    def update_sat(self):
        resp = requests.get(UPDATE_URL)
        data = resp.json()

        raw_rate = data['bpi']['EUR']['rate']
        rate = float(raw_rate.replace(',', ''))

        euro_cent_price = 50
        price = euro_cent_price/(rate*100)

        return price

