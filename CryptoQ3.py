import requests
import json
api = "https://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.5324296645627815&marketId=1&code=000001&language=EN"


apijson = requests.get(api)
temp = apijson.json()

data2 = json.dumps(temp)
data1 = json.loads(data2)
high = data1["data"]["high"]
low = data1["data"]["low"]

def ver_statuscode():
    if apijson.status_code == 200:
        print("Response status success")
    else:
        print ("failed")

def ver_highlow():
    if high >= low:
        print ("Verified data, High > Low")
    else:
        print("Data damaged")

    
print (apijson.status_code)
ver_statuscode()
print (high, low)   
ver_highlow()