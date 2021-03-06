from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import shlex
from time import sleep, strptime
import numpy as np
from numpy import average
import paramiko
from re import findall
from math import ceil, floor

def local_cmd(command):
    stdout = Popen(command, shell=True, stdout=PIPE).stdout
    return stdout.read()

def ssh_connect(host):
    k = paramiko.RSAKey.from_private_key_file(".ssh/my-ssh-key")
    ssh = paramiko.SSHClient()
    print "connecting"
    name="vadisaf"
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(username=name, hostname = host, pkey = k)
    print "connected"
    return ssh

def ssh_cmd(command, ssh):
    output = ""
    stdout = ssh.exec_command(command)[1]
    for line in stdout:
        output += line
    if (len(output) > 0):
        return output
