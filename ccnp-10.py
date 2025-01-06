from netaddr import IPAddress,IPNetwork

ip_info = IPNetwork('192.168.1.1/25')

print(ip_info.broadcast)
print(ip_info.cidr)
print(ip_info.hostmask)
print(ip_info.ip)
print(ip_info.size)
print(ip_info.netmask)