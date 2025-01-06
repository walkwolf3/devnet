import requests
from requests.auth import HTTPBasicAuth


url = "https://192.168.32.210/restconf/data/ietf-interfaces:interfaces/"
auth_info = HTTPBasicAuth("cisco","cisco")
payload={}
headers = {
    'Authorization':auth_info
}

response = requests.request("GET",url=url,verify=False,data=payload,headers=headers)
print(response)