from __future__ import absolute_import, division, print_function
import netmiko
import json

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': 'ip_address',  
    'username': 'username',
    'password': 'password',
    }


interface = input("Enter the interface you want to default: ")

# Connect to the device
connection = netmiko.ConnectHandler(**device)

# Define the commands to default the interface
commands = [
    f"do show clock",
    f"default interface {interface}",
    f"interface {interface}",
    "description ****** unused",
    f'shutdown',
    f"do show interface {interface} description",
    f"do show clock"
]

print(f"Connecting to {device['ip']}") 

# Send the commands
output = connection.send_config_set(commands, delay_factor=2)

print('='*79)
print(output)
print('='*79)


# Write block
write = input(f"do you want to write changes? Yes/No: ")

write = write.upper()

while write not in ["YES", "NO"]:
    write = input(f"Enter 'YES' or 'NO': ")
    write = write.strip().upper()

print('='*79)

if write == "YES":
    write_output = connection.send_command("write")
if write == "NO":
    print("Configuration changes not written")

# Disconnect from the device
connection.disconnect()