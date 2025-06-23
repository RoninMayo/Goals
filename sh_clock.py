#!/bin/bash

from __future__ import absolute_import, division, print_function
import netmiko
import json

devices = [

 {'ip': '192.168.1.30', 
		'device_type': 'cisco_ios',
		'username': 'admin',
		'password': 'sd$%1321'},
	   
#  {'ip': '192.168.2.1', 
# 		'device_type': 'cisco_ios',
# 		'username': 'admin',
# 		'password': 'automate'},
	   
# {'ip': '192.168.1.254', 
# 		'device_type': 'cisco_ios',
# 		'username': 'admin',
# 		'password': 'automate'},
	   
# {'ip': '192.168.2.254', 
# 		'device_type': 'cisco_ios',
# 		'username': 'admin',
# 		'password': 'automate'},
]
devices.__doc__
# devices.strip().splitlines()
# print(devices)
# netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                    #   netmiko.ssh_exception.NetMikoTimeoutException)

for device in devices:
    try:
        print('='*79)
        print(f"Connecting to {device['ip']}") 
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('show run'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print(f"Failed to {device['ip']} \n {e}")
