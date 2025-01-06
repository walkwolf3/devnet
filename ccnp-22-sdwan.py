import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

headers = {"content-Type": "application/x-www-form-urlencoded"}
payload = {"j_username":"devnetuser","j_password":"RG!_Yw919_83"}
url = "https://sandbox-sdwan-2.cisco.com/j_security_check"

response = requests.post(url, headers=headers, data=payload, verify=False)

cookie = response.headers["set-cookie"]
JSESSIONID = cookie.split(";")[0]
#print(JSESSIONID)

url2 = 'https://sandbox-sdwan-2.cisco.com/dataservice/device'
headers2 = {"Cookie": JSESSIONID,
            "content-Type": "application/json"
}

response2 = requests.get(url=url2,headers=headers2,verify=False)
print(json.dumps(response2, indent=4))





