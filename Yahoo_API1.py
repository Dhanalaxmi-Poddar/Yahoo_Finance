import json
import requests
import pprint

url='https://yfapi.net/v6/finance/quote'
headers={'x-api-key':"dmdtbB7cBwYDb2EhFykra5YzdCGdyAAa6BO1xIL6"}
querystring={"symbols":input("Stock Symbol:")}

data=requests.request("GET",url,headers=headers,params=querystring)

data_read=((data.json().get('quoteResponse').get('result')))

for data_name in data_read:
    print('The previous market close price is',data_name['regularMarketPreviousClose'])