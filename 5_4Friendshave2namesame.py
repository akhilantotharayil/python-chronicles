''' progeam6: Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use key as their names.Asume that the names are unique
if the names  of 2 friends are same;what will happen to the program in problem 6?
'''

d = {}

name = input("Enter the name: ")
lang = input("Enter the language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the friends language: ")

print(d)

''' Enter the name: Akhil
Enter the language: java
Enter friends name: Saurabh
Enter the friends language: C++
Enter friends name: Saurabh
Enter the friends language: Java
Enter friends name: Pranavi
Enter the friends language: Java
Enter friends name: Suhas
Enter the friends language: Spring Boot
Enter friends name: Ramesh
Enter the friends language: Odoo
Enter friends name: Ravi
Enter the friends language: Cobalt
{'Akhil': 'java', 'Saurabh': 'Java', 'Pranavi': 'Java', 'Suhas': 'Spring Boot', 'Ramesh': 'Odoo'}

if names of  same is there  it skips the first one and shows the second one as unique
'''