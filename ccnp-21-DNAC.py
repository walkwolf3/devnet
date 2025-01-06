import requests
from requests.auth import HTTPBasicAuth
import json
import sys

requests.packages.urllib3.disable_warnings()

#Cisco DNAC

"""
DNA_CENTER = {
    "hosts": "sandboxdnac.cisco.com",
    "port": "443",
    "username": "devnetuser",
    "password": "Cisco123!"
}
"""

#url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
#url ='https://' + DNA_CENTER['hosts'] + '/dna/system/api/v1/auth/token'

def Get_Dnac_Token():
    DNA_CENTER = {
    "hosts": "sandboxdnac.cisco.com",
    "port": "443",
    "username": "devnetuser",
    "password": "Cisco123!"
    }
    url ='https://' + DNA_CENTER['hosts'] + '/dna/system/api/v1/auth/token'
    try:
        response1 = requests.post(url,auth=HTTPBasicAuth(DNA_CENTER['username'],DNA_CENTER['password']),verify=False)
        token = response1.json()['Token']
    except:
        print(f"Status: {response1.status_code}")

    return token

def Get_Device_List(token):
    url2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    headers = {
    "x-auth-token": token
    }
    try:
        response2 = requests.get(url2,headers=headers,verify=False)
        return response2.json()
    except:
        print(f"Status: {response2.status_code}")


token = Get_Dnac_Token()    
response2 = Get_Device_List(token)

#print(json.dumps(response2.json()["response"], indent=4))

def Get_Device_IP_Hostname(response):
    #print(response['response'])
    for i in response['response']:
      print(f"Device's host name is: {i['hostname']} and IP is: {i['managementIpAddress']}")
    #print(type(response))

Get_Device_IP_Hostname(response2)

def Get_Device_Health(token):
    url3 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"
    headers = {
    "x-auth-token": token
    }
    try:
        response2 = requests.get(url3,headers=headers,verify=False)
        return response2
    except:
        print(f"Status: {response2.status_code}")

response = Get_Device_Health(token)
print(json.dumps(response.json()["response"], indent=4))
