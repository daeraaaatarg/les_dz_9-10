# важко було зробити самій тому попросила чат джпт
# код працює, я в ньому розібралась

import requests
import xml.etree.ElementTree as ET

class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&xml'
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Couldn't find currency")

        root = ET.fromstring(response.content)
        for currency in root.find_all('currency'):
            rate = currency.find('rate').text
            return float(rate)

    def convert_to_usd(self, amount_uah):
        return round(amount_uah / self.usd_rate, 2)

if __name__ == "__main__":
    amount_uah = float(input("Input amount of money in hryvnas: "))
    converter = CurrencyConverter()
    amount_usd = converter.convert_to_usd(amount_uah)
    print(f"{amount_uah} hry ≈ {amount_usd} USD (currency: {converter.usd_rate} hry/USD)")