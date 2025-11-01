'''Write a program to find mine a log file and find out whether it contians 'python' '''

with open("log.txt") as f:
    content = f.read()

if ("Python" in content):
    print("Yes python is present")
else:
    print("No Python is present")
