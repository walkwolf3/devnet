from textfsm import TextFSM
from netmiko import ConnectHandler
from netmiko import SSHDetect
import json


device_info = {'device_type':'cisco_xe',
                    'host':192.168.32.200',
                    'username':'cisco',
                    'password':'cisco',
                    'secret':'cisco',
                    'port':'22'
                    }

ssh_conect = ConnectHandler(**device_info)


with open('interface.textfsm','r') as f:
    template = TextFSM(f)


output = '''
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.1.1     YES manual up                    down
Ethernet0/1                172.16.1.1      YES unset  administratively down down
Ethernet0/2                unassigned      YES unset  administratively down down
Ethernet0/3                unassigned      YES unset  up                    up
Ethernet1/0                12.1.1.1        YES unset  up                    dwon
Ethernet1/1                13.1.1.1        YES unset  up                    up
Ethernet1/2                14.1.1.1        YES unset  up                    down
Ethernet1/3                15.1.1.1        YES unset  up                    up
GigabitEthernet0/0         172.16.2.1      YES unset  up                    down
GigabitEthernet0/0         172.16.2.1      YES unset  up                    up
Loopback0                  1.1.1.1         YES manual up                    down
'''

interfaces = template.ParseText(output)
for i in interfaces:
    print(i)