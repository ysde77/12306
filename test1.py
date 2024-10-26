import requests
station_url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9320"
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    # "Referer":"https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2024-09-23&flag=N,N,Y"
    }
resp=requests.get(station_url,headers=headers)
s_data=resp.text[resp.text.find('='):-1]
s_data=s_data.split("|")
num=len(s_data)//5
station_name={}
k1=1
k2=2
for i in range(num):
    station_name[s_data[k1]]=s_data[k2]
    k1 +=5
    k2 +=5
print(station_name)