import csv, operator, glob, json, pprint, urllib, urllib.request, math, codecs

class OasisDexAPI:
    @staticmethod
    def orderbook(symbol):
        url = "http://api.oasisdex.com/v1/orders/" + symbol
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        return data

print(OasisDexAPI.orderbook("ETH/DAI"))
