from napalm import get_network_driver
import json

ios_driver = get_network_driver('ios')

with ios_driver("192.168.32.200","cisco","cisco",optional_args={"secret":"cisco"}) as output:
    print(json.dumps(output.get_interfaces_ip()))




