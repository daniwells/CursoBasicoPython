import requests

requisition = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#print(requisition)
#print(requisition.json())

requisition_dic = requisition.json()

print(requisition_dic['EURBRL']['bid'])