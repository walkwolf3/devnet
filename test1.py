from netmiko import ConnectHandler
from netmiko import SSHDetect

def Get_Device_Info(ipaddr,devicetype,username,password,secret):

    device_info = {'device_type' : devicetype,
            'host':ipaddr,
            'username':username,
            'password':password,
            'secret':secret,
            'port':'22'
            }
    return device_info

def Ssh_Connect(device_info):
        ssh_connect = ConnectHandler(**device_info)
        output = ssh_connect.send_command('show ip int brie')
        return output

device_info = Get_Device_Info(ipaddr='192.168.32.200',
                            devicetype='cisco_ios',
                            username='cisco',
                            password='cisco',
                            secret='cisco')


output = Ssh_Connect(device_info=device_info)
print(output)






