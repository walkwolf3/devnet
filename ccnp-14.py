from ncclient import manager

subtree = '''
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces:
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
</filter>

'''


with manager.connect(host = "192.168.32.210",
                    port = "830",
                    username = "cisco",
                    password = "cisco",
                    hostkey_verify = False,
                    device_params = {"name":"iosxe"}) as device01:
    device01_config = device01.get_config(source = "running")
print(device01_config)