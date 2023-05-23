import requests


class Skinport:

    def initRequest(self):
        URL = 'https://api.skinport.com/v1/items'
        params = {
            "app_id": 730,
            "currency": "USD",
            "tradable": 0,
        }
        res = requests.get(URL, params=params).json()

        return res

    def getSkinportData(self, res):

        list_of_items = []

        for item in res:
            name = item["market_hash_name"]
            price = item["min_price"]
            currency = item["currency"]
            link = item["item_page"]
            item_data = [name, price, currency, link]
            list_of_items.append(item_data)
        else:
            print("Nieprawidłowe dane w odpowiedzi API.")

        return list_of_items




