import requests
import json
import urllib3
urllib3.disable_warnings()

url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
payload = """
{
    "aaaUser":{
        "attributes":{
            "name":"admin"
            "pwd":"!v3G@!4@Y"
        }
    }
}

"""
headers = {"Content-Type":"text/plain"}
response = requests.request('POST',url,headers=headers,data=payload,verify=False)
r = response.json()
print(f'{r}\n')

token = r['imdata'][0]['aaaLogin']['attributes']['token']

print(token)