import os #importing os module

print("Space of the system is ",os.system('df -h'))
print("System is running since ",os.system('uptime'))
print("Listing files  of /opt directory ",os.system('ls -la /opt/'))
print("Checking RAM consumption ",os.system('free -h'))
