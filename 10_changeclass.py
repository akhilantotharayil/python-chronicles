'''Write a  class Train which has methods to book a ticket,get status of(no of seats) and get fare information of 
train running under Indian Railways.
Can you change the self-paramter inside a class to something else(say"akhil").Try changing self to "slf" or "akhil" 
and see the effects.Program is saved as 10 classattribute.py'''

from random  import randint


class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def  book(akhil,fro,to):
        print(f"Ticket is booked in train no: {akhil.trainNo} from {fro} to {to}")


    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket  fare  in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")



t = Train(12399)
t.book("LTT","Mumbai")
t.getStatus()
t.getFare("LTT","Mumbai")

#It is running after chnaging but est practice keep self this is the standard practice.