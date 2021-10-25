import json
import requests
import pprint
import urllib3

url='https://yfapi.net/v6/finance/quote'
headers={'x-api-key':"dmdtbB7cBwYDb2EhFykra5YzdCGdyAAa6BO1xIL6",
         "User-Agent":"Defined"}
querystring={"symbols":input("Stock Symbol:")}

data=requests.request("GET",url,headers=headers,params=querystring)

data_read=((data.json().get('quoteResponse').get('result')))

#pprint.pprint(data.json().get('quoteResponse').get('result'))

for data_name in data_read:
    print('The previousMarketclosePrice is',data_name['regularMarketPreviousClose'])