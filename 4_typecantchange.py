'''Check that a tuple type cannot be chnaged in python'''

a = (34,234,"Akhil")

a[2]= ("Nikhil")


#TypeError: 'tuple' object does not support item assignment
