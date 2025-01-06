from test1 import Get_Device_Info
from test1 import Ssh_Connect

device_info = Get_Device_Info(ipaddr='192.168.32.200',
                            devicetype='cisco_ios',
                            username='cisco',
                            password='cisco',
                            secret='cisco')
                            
output = Ssh_Connect(device_info=device_info)
print(output)


'''
device = {'device_type' : 'autodetect',
         'host':'192.168.32.200',
         'username':'cisco',
         'password':'cisco',
         'secret':'cisco',
         'port':'22'
         }


detect01 = SSHDetect(**device)
detect01_type = detect01.autodetect()

print(detect01_type)
'''



#conn = ConnectHandler(**Get_Device_Info)


'''
command_list = ['int lo0','ip address 1.1.1.1 255.255.255.0']
#output = conn.send_config_set(command_list)

#output = conn.send_config_set('show ip int brie',strip_prompt=False,strip_command=False,delay_factor=2)

#print(output)
#print(conn)
'''
#conn.disconnect()


