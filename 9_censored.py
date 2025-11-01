'''A file contains a word "Donkey" multiple times.You need to write a program
 which replace this word with #### by updating the same file.
 Repeat this program with for a list of such words to be censored'''

words = ["Bastard","Chaava","Rascal"]

with open("file1.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("file1.txt","w") as f:
    f.write(content)
