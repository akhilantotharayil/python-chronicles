'''Create a class with a class attribute a;create an object  from it and set 'a'  directly using  object.a = o.Does this change the class attribute? Program saved as 10 classattribute.py '''

class Demo:
    a = 4


o = Demo()
print(o.a)
o.a = 0 
print(o.a)
print(Demo.a)


'''Setting o.a = 0 does not change the class attribute Demo.a.
It only creates or updates an instance attribute that shadows the class attribute for that specific object.'''