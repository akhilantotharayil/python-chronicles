'''Create a class "Programmer" for storing information of few programmers working at Microsoft. Program saved as 10 programmer.py '''
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Akhil",1200000,245001)
print(p.name,p.salary,p.pin,p.company)

r = Programmer("Sandeepkumar",2500000,400088)
print(r.name,r.salary,r.pin,r.company)
