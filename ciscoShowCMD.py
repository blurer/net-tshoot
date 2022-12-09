#!/usr/bin/env python3
from netmiko import ConnectHandler

# to prevent using hardcoded passwords
from getpass import getpass
getPassword = getpass()

# add relevant ip addresses (or import csv and add csv here)
ipam = {
    "172.17.228.204"
}

# input the commands to run
command = {
    "show ip int brief",
    "show version | in uptime",
    "show ip route | be Gateway"
}

# this runs above commands on the above ip addresses
for i in ipam:
    cisco1 = { 
        "device_type": "cisco_ios",
        "host": i,
        "username": "bl",
        "password": getPassword
    }
    # Show command that we execute.
    for c in command:
	    with ConnectHandler(**cisco1) as net_connect:
	        output = net_connect.send_command(c)

    # Automatically cleans-up the output so that only the show output is returned
	    print('#'*64)
	    print(i, " - ", c)
	    print('#'*64)
	    print(output)
	    print()

