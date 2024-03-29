from __future__ import absolute_import, division, print_function
import netmiko
import json


# import credentials from JSON
with open('/path/to/credentials.json', 'r') as f:
    devices = json.load(f)


interface = input("Enter the interface you want to bounce: ")

# Define presnapshot commands
snapcommands = [

f'show interface {interface} description',
f'show run interface {interface}',
f'show clock'

]


# Gather presnapshot
for device in devices:
    print('*'*79)
    print(f"Gathering snapshot of {interface} on {device['ip'] }")
    print('*'*79)
    connection = netmiko.ConnectHandler(**device)
    for snapc in snapcommands:
        presnap = connection.send_command(snapc)
        print(presnap)
    connection.disconnect()


# Define commands to bounce the interface
commands = [
    f"interface {interface}",
    # f"do show interface {interface} description"
    f'shutdown',
    f'no shutdown',
    f"do show interface {interface} description"
    # f"do show log | include {interface}"

]

# Connect to the device and send the commands
for device in devices:
    print('='*79)
    print(f'Connecting to device {device['ip']}')
    connection = netmiko.ConnectHandler(**device)
    output = connection.send_config_set(commands)
    print('='*79)
    print(output)

# Disconnect from the device
connection.disconnect()