'''Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use key as their names.Asume that the names are unique'''

d = {}
name = input("Enter the name: ")
lang = input("Enter Language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

print(d)
