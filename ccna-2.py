from ncclient import manager
from lxml import etree

device = manager.connect(host='192.168.32.210',
                        port=830,
                        username='cisco',
                        password='cisco',
                        hostkey_verify=False,
                        device_params={'name':'iosxe'}
)


config = device.get_config(source='show ip int brie')
print(config)
