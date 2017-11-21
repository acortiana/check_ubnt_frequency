#!/usr/bin/env python

import sys, paramiko, argparse

description = """Checks if the current frequency value has changed from the expected value.
This is done via ssh passwordless connection
"""

username = "ubnt"
port = 22
command = 'iwconfig ath0 | grep Frequency | sed "s/^.*Frequency://" | sed "s/ .Hz .*$//"'

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-H", "--hostname", help="IP Address / Hostname to check [REQUIRED]",type=str, required=True)
parser.add_argument("-e", "--expected_frequency",help="Expected frequency value [REQUIRED]",type=str,required=True)
parser.add_argument("-u", "--username", help="SSH Username",type=str, default="ubnt")
parser.add_argument("-p", "--port", help="SSH port", type=int, default=22)

args = parser.parse_args()
username = args.username
port = args.port
hostname = args.hostname
expected_frequency = args.expected_frequency

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(hostname, port=port, username=username)

    stdin, stdout, stderr = client.exec_command(command)
    curfrequency = stdout.read().rstrip()
    print "Current frequency: " + str(curfrequency) + "   Expected frequency: " + str(expected_frequency)
    if str(curfrequency) == str(expected_frequency):
        sys.exit(0)
    else:
        sys.exit(2)

finally:
    client.close()
