import os

command = "ls -la"
command = "df -h"
command = "free -h"

def system_directory(command):
    print(os.system(command))

def system_space(command):
    print(os.system(command))

def system_ram(command):
    print(os.system(command))

#system_directory("uptime")
system_space("df -h")
#system_ram("free -h")