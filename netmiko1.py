from netmiko import ConnectHandler

ios_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.254',
    'username': 'admin',
    'password': 'cisco',
}
net_connect =ConnectHandler(**ios_l2)
output = net_connect.send_command('show ip int brief')
print (output)

net_connect =ConnectHandler(**ios_l2)
output = net_connect.send_command('show version')
print (output)

## It is working properly