import requests
import json

lis = []
parkingName = ""
addr = ""
tel = ""

def search(search):
    global lis
    global parkingName
    global addr
    global tel
    global cnt

    lis = []

    url = "http://openapi.seoul.go.kr:8088/4e6643576861687339355165484770/json/GetParkInfo/1/5/%7B%7D%22.format(search)"
    res = requests.get(url)
    res = res.text
    res = json.loads(res)
    try :
        for i in range(10):
            parkingName = res["GetParkInfo"]["row"][i]["PARKING_NAME"]
            addr = res["GetParkInfo"]["row"][i]["ADDR"]
            tel = res["GetParkInfo"]["row"][i]["TEL"]
            lis.append([parkingName,addr,tel])
    except:
        pass