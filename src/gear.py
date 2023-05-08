import requests
import json

lis = []
parkingName = ""
addr = ""
tel = ""
payNm = ""

def search(search):
    global lis
    global parkingName
    global addr
    global tel
    global payNm

    lis = []

    url = "http://openapi.seoul.go.kr:8088/4e6643576861687339355165484770/json/GetParkInfo/1/5/{}".format(search)
    res = requests.get(url)
    res = res.text
    res = json.loads(res)
    try :
        for i in range(5):
            parkingName = res["GetParkInfo"]["row"][i]["PARKING_NAME"]
            addr = res["GetParkInfo"]["row"][i]["ADDR"]
            tel = res["GetParkInfo"]["row"][i]["TEL"]
            payNm = res["GetParkInfo"]["row"][i]["SATURDAY_PAY_NM"]
            lis.append([parkingName,addr,tel,payNm])
    except:
        pass