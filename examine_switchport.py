from __future__ import absolute_import, division, print_function
import netmiko
import json

# Define device parameters
devices = {
    'device_type': 'cisco_ios',
    'ip': 'ip_address',  
    'username': 'username',
    'password': 'password',
    }


print('=' * 79, '\n')

# User input for interface
interface = input("Enter the interface you want to examine: ")

# priv = int(input(f"What priv level? "))

# Connect to the device
connection = netmiko.ConnectHandler(**devices)

print('=' * 79, '\n')

print(f"Results of {interface} query: ")

# Set timestamp
# time = connection.send_command(f"show clock")


# Define commands to examine the interface
commands = [
    
    f"show clock",
    f"show interface {interface} status",
    f"show mac add interface {interface}",
    f"show interface {interface} description",
    f'show power inline {interface}',
    f'show run interface {interface}',
    # f"show interface {interface} detail"
    f"show clock"

]


for command in commands:
    output = connection.send_command(command)
    print('=' * 79, '\n')
    print(output)
print('=' * 79, '\n')


# Close the connection
connection.disconnect()