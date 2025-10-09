'''Write a program to fill in a letter template given below with name and date
letter = ''
        Dear <|Name|>
        You are selected!
        <|Date|>
        ''
        
'''


Name = input("Enter  your name: ")
Date = input("ENter the Date: ")

letter = '''
        Dear <|Name|>
        You are selected!
        <|Date|>
        '''

print(letter.replace("<|Name|>","Akhil").replace("<|Date|>", "24 October 2025"))
