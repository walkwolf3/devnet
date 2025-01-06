import requests
import json

url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload = "{\r\n  \"aaaUser\" : {\r\n    \"attributes\" : {\r\n      \"name\" : \"admin\",\r\n      \"pwd\" : \"!v3G@!4@Y\"\r\n    }\r\n  }\r\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

response_json = response.json()

token = response_json["imdata"][0]["aaaLogin"]["attributes"]["token"]

url2 = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"

payload2 = {}
headers2 = {
    "content-type": "application/json",
    "Cookie": "APIC-Cookie="+token
    }

response2 = requests.request("GET", url2, data=payload2, headers=headers2, verify=False)
print(response2)

payload3 = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-lc1\",\"status\":\"created\"},\"name\":\"tn-lc1\",}}}"
headers3 = {
    "content-type": "application/json",
    "Cookie": "APIC-Cookie="+token
    }

url3 = "https://sandboxapicdc.cisco.com/api/node/mo/uni.json"
payload4 = json.dumps(payload3, indent = 4)
response3 = requests.post(url3, data=payload4, headers=headers3, verify=False)

print(response3)
