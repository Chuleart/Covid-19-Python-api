import requests
import time


#pip install requests
#print(f'requests version: {requests.__version__}')

timeis = time.localtime()
date = time.strftime('%d/%m/%Y',timeis)
total = date,"00:00"


response=requests.get("https://covid19.th-stat.com/api/open/today")
data=response.json() 


print("รายงานของวันที่ :" ,data["UpdateDate"])
print("ติดเชื้อสะสม    :" ,data["Confirmed"])
print("รักษาหายแล้ว   :" ,data["Recovered"])
print("รักษาในโรงบาล  :" ,data["Hospitalized"])
print("ตาย           :" ,data["Deaths"])


caseresponse = requests.get("https://covid19.th-stat.com/api/open/cases/sum")
datacase     = caseresponse.json() 
for i,(k,v) in enumerate(datacase["Province"].items()):
    print(i,k,v)