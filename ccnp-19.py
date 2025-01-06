import requests
from requests.auth import HTTPBasicAuth

#url = "https://192.168.32.210/restconf/data/Cisco-IOS-XE-native:native/router-bgp/bgp"
#url = "https://192.168.32.210/.well-known/host-meta"
url = "https://192.168.32.210/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
payload = {}
auth_info = HTTPBasicAuth('cisco','cisco')

headers = {
}

#response = requests.get(url=url,headers=headers,data=payload,verify=False,auth=auth_info)
response = requests.request("GET",url=url,headers=headers,data=payload,verify=False,auth=auth_info)
print(response.text)
