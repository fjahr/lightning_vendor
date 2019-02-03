import requests
import time
import threading

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

class PriceUpdater:
    def __init__(self, vendor):
        self.interval = 5
        self.vendor = vendor

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            time.sleep(self.interval)
            self.vendor.price = Price().update_mbtc()

            print(datetime.datetime.now().__str__() + ' : Updated Price ' + self.vendor.price)

