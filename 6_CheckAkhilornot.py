'''Write a program to find out whether a given post is talking about "Akhil" or not.'''

post= input("Enter the post: ")

name = input("Enter the name: ")

if name.lower() in post.lower():
    print("yes this post is talking about Akhil")

else:
    print("yes this post is talking about Akhil :(")
