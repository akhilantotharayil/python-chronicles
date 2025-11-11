'''Create a class 'Pets' from a class 'Animals and further create a class 'Dog' from  'Pets'.Add a method 'bark' 
to class 'Dog'.Program saved as 11_Pets.py '''

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    pass
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()

