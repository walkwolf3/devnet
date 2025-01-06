from ncclient import manager
from lxml import etree

interface_yang_template = open('ccnp-16.xml','r').read()

subtree = interface_yang_template.format(int_type = 'GigabitEthernet',
                                        int_name = '2',
                                        int_ip = '1.1.1.1',
                                        int_mask = '255.255.255.255')


print(subtree)

with manager.connect(host='192.168.32.210',
                    port = '830',
                    username = 'cisco',
                    password = 'cisco',
                    hostkey_verify = False,
                    device_params = {"name":"iosxe"}) as device01:
                    
    config = device01.get_config(subtree)
    print(config)