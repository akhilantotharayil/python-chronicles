#Get input from user
name=input("Enter your name")

#Length of the string
print("Length of the string",len(name))

#COnvert to lower case

print("Lowercase:",name.lower())

#Convert to upper case
print("Uppercase:",name.upper())

#Replace a string
replace_string=name.replace("A","@")
print("Replaced String is",replace_string)

#Find a substring
position=name.find("k")
if position !=1:
    print("SUbstring is found at index:",position)
else:
    print("Substring is not found")


#strip whhitespace
stripped=name.strip()
print("String with no leading/trailing spaces:",stripped)



