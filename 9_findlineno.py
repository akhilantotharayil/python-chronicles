'''Write a program to find mine a log file and find out whether it contians 'python'
Find the line number where  Keyword Python is printed '''



with open("log.txt") as f:
    lines = f.readlines()

lineno  = 1
for line in lines:
    if ("Python" in line):
        print(f"Yes python is present.Line number is: {lineno}")
    else:
         print("No Python is present")
    lineno += 1
