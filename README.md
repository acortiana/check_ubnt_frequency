This nagios check verifies if the current radio frequency value has changed
from the expected value on AirOS ubiquity devices.
This is done via ssh passwordless connection.
This is usually used to detect frequency changes caused by DFS operations.
Depends on:
  - python 2
  - argparse python library
  - paramiko python library

On Ubuntu:
sudo apt-get install python-paramiko

On CentOS:
yum install python-argparse
yum install python-paramiko

WARNING:
The program auto-adds the target host ssh keys to the local known_hosts database
