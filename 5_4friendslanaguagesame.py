''' progeam6: Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use key as their names.Asume that the names are unique
if the names  of 2 friends having same language ;what will happen to the program in problem 6?
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


'''Ans: It will print the same languages as Python dictionaries allow duplicate values. '''