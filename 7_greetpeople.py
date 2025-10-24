'''Write a program to greet all the person names whose name stored in a list 'l' and which starts with S.
l = ["Harry","Sohan","Sachin","Rahul"] '''

l = ["Harry","Sohan","Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
    else:
        print("Not found Mone!")
