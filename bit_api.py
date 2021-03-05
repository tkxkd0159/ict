import requests as req
import json

TYPE = "BTC"



if TYPE == "BTC":
    ### Use API
    # r = req.get("https://bitnodes.io/api/v1/snapshots/1614660691/")
    # print(type(r))
    # data = r.json()

    # with open('bit_node.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    with open('bit_node.json', 'r') as f:
        data = json.load(f)
    print(data)



if TYPE == "ETH":
    r = req.get("https://api.etherscan.io/api?module=stats&action=nodecount&apikey=PRGDW4IBEHUZKTMZAZWM2EMY9HKA9HI4GV")
    data = r.json()
    print(data)