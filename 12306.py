#12306查工具
import requests
begin_addr="合肥"
end_addr="北京"
start_time="2024-09-24"
#获取城市信息
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
#获取票信息
ba=station_name.get(begin_addr)
ea=station_name.get(end_addr)

info_url=f"https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={start_time}&leftTicketDTO.from_station={ba}&leftTicketDTO.to_station={ea}&purpose_codes=ADULT"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "Cookie":"_uab_collina=172709030282227605084403; JSESSIONID=F45FE38BB62511FF5F82AA0F582DD928; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_wfdc_flag=dc; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2024-09-24; _jc_save_toDate=2024-09-24; BIGipServerotn=1961361674.50210.0000; BIGipServerpassport=870842634.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u5317%u4EAC%u5357%2CVNP"
}
resp=requests.get(info_url,headers=header)
resp_data=resp.json().get("data").get("result")
for r in resp_data:
    data=[a for a in r.split("|")]
    if data[1]!="列车停运":
        print(f"{data[13]}--发车{data[8]}--{data[6]}--{data[7]}--特等座{data[32]}--{data[31]}")
    # for t in r.split('|'):
    #     print(t)
    # break
    #     # print(r)