from Skinport import Skinport
from Buff import Buff
import json

with open("steam.json", "r") as f:
    config = json.load(f)


#object initiation
spClass = Skinport()
bClass = Buff(config["Cookies"])

#skinPort
sp_response = spClass.initRequest()
sp = spClass.getSkinportData(sp_response)

#buff
for item in sp:

    item_name = item[0]  # Wyodrębnij nazwę przedmiotu
    item_price_skinPort = item[1]
    item_currency = item[2]
    print(item_name, item_price_skinPort, item_currency)


    b_response = bClass.initRequest(item_name)
    b = bClass.getBuffData(b_response)
