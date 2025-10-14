'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') #length of s after these operations?

'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)


'''20 and 20.0 are same there are considered as one  and other one is tring 20 thats why in out it is shwoing as 2 i.e {20, '20'}'''
