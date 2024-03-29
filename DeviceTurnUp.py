# Initial config of device (users + SSH required)

from __future__ import absolute_import, division, print_function
import netmiko
import json

# Define device parameters
devices = [
    {
    'device_type': 'cisco_ios',
    'ip': 'ip_address',  
    'username': 'username',
    'password': 'password',
    },

    {
    'device_type': 'cisco_ios',
    'ip': 'ip_address',  
    'username': 'username',
    'password': 'password',
    }
]

print('=' * 79, '\n')
print(f"This script will configure:")
print(f"-Logging\n-Basic Security\n-NTP\n-Banner\n-VTY Lines\n-Syslog")
print('=' * 79, '\n')

commands = [
    f"service password-encryption",
    f"ntp server ntp_server_ip",
    f"ntp server ntp_server_ip",
    f"ntp logging",
    f"logging buffered 20000 debugging",
    f"service timestamps log datetime msec localtime show-timezone",
    f"logging console debugging",
    f"ip ssh logging events",
    f"logging host ntp_server_ip",
    f"logging trap debugging",
    f"banner motd #=== Authorized Access Only === #",
    f"banner login #=== Unauthorized Use is Prohibited ===#",
    f"line vty 0 4",
    f"login local",
    # f"exec prompt timestamp",
    f"transport input ssh"
]


# Send the commands and print
for device in devices:
    connection = netmiko.ConnectHandler(**device)
    print('=' * 79, '\n')
    print(f"Connecting to {device['ip']}")
    print('=' * 79, '\n')
    output = connection.send_config_set(commands)
    print(output)
    connection.disconnect()

# Transition to verify block
print('=' * 79, '\n', '\n')
print("Verification Commands After This")
print('\n', '\n', '='*79)

# Verify Block
verify = [
    f"show run | include password-enc",
    f"show run | include ntp",
    f"show run | include logging buff",
    f"show run | include logging console",
    f"show run | include banner",
    f"sh run | i log"
    f"sh run | b vty",
]

for device in devices:
    connection = netmiko.ConnectHandler(**device)
    print(f"Connecting to {device['ip']}")
    for verif in verify:
        voutput = connection.send_command(verif)
        print('=' * 79)    
        print(verif)
        print('=' * 79)    
        print(voutput)
        print('=' * 79, '\n')
    connection.disconnect()
print('=' * 79, '\n')  


# Write block
for device in devices:
    connection = netmiko.ConnectHandler(**device)
    print(f"Connecting to {device['ip']}")
    write = input(f"do you want to write changes? Yes/No: ")
    write = write.strip().upper()
    while write not in ["YES", "NO"]:
        write = input(f"Enter 'YES' or 'NO': ")
        write = write.strip().upper()
    if write == "YES":
        write_output = connection.save_config()
        print("Configuration changes written")
        print('='*79, '\n')
    if write == "NO":
        print("Configuration changes not written")
        print('='*79, '\n')
    connection.disconnect()
