from netmiko import ConnectHandler
from netmiko import SSHDetect
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
import time

def Get_Device_Info(ipaddr,username,password,secret):
    device_info = {'device_type':'autodetect',
                    'host':ipaddr,
                    'username':username,
                    'password':password,
                    'secret':secret,
                    'port':'22'
                    }
    return device_info

def Get_Device_Type(device_info):
    cisco_device_type = SSHDetect(**device_info)
    device_type = cisco_device_type.autodetect
    return device_type

def Mod_Device_Type(device_type,device_info):
    device_info['device_type'] = device_type


def Ssh_Connect(device_info):
        ssh_connect = ConnectHandler(**device_info)
        output = ssh_connect.send_command('show ip int brie')
        return output

with open('devicelist.txt','r') as f:
    str1 = f.read()
    list1 = str1.split('\n')
    print(list1,type(list1))
    for device in list1:
        device=device.split(' ')
        print(device)
        device_info = Get_Device_Info(device[0],device[1],device[2],device[3])
        print(device_info)
        device_type = Get_Device_Type(device_info)
        output = Ssh_Connect(device_info)
        print(output)

