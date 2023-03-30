import requests
import json

city = "신내"
url = "http://openapi.seoul.go.kr:8088/4e6643576861687339355165484770/json/GetParkInfo/1/5/{}".format(city)
res = requests.get(url)
res = res.text
res = json.loads(res)

try :
    for i in range(10):
        parkingName = res["GetParkInfo"]["row"][i]["PARKING_NAME"]
        addr = res["GetParkInfo"]["row"][i]["ADDR"]
        tel = res["GetParkInfo"]["row"][i]["TEL"]
        payNm = res["GetParkInfo"]["row"][i]["PAY_NM"]

        print(parkingName,addr,tel,payNm)
        print("---------- ----------")
except:
    pass

