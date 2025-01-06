from netmiko import ConnectHandler
from netmiko import SSHDetect
from devicelist import *


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

def Mod_Device_Type(device_type):
    device_info['device_type'] = device_type


def Ssh_Connect(device_info):
        ssh_connect = ConnectHandler(**device_info)
        output = ssh_connect.send_command('show ip int brie')
        return output

device_info = Get_Device_Info(ipaddr='192.168.32.200',username='cisco',password='cisco',secret='cisco')
device_type = Get_Device_Type(device_info)
#Mod_Device_Type(device_type)


output = Ssh_Connect(device_info)
print(output)
print(device_info)


