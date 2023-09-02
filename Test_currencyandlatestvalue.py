
import requests
import json

url = "https://api-pub.bitfinex.com/v2/tickers?symbols=ALL"
response = requests.get(url)

print(response.status_code)

data = response.json()

# print(data)
#
# print(data[0][0])
# print(data[0][4])
# print(len(data))
l = len(data)

dic1 = {}

for x in range(0, l):
    symbol = data[x][0]
    exp_cur = data[x][4]
    dic1.update({symbol: exp_cur})

print("Dictionary Info (Currency symbol : latest value):", dic1)


