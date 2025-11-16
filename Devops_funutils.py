import os
import datetime

command = "ls -la"
command = "df -h"
command = "free -h"

def system_directory(command):
    print(os.system(command))

def system_space(command):
    print(os.system(command))

def system_ram(command):
    print(os.system(command))

def system_time():
    return datetime.datetime.today()

today = system_time()
print(today)

#system_directory("uptime")
#system_space("df -h")
#system_ram("free -h")