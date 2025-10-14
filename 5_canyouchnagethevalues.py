'''Can you change the values inside a list which is contained in set S ?
 s = {8,7,12,"Harry",[1,2]}
   '''

s = {8,7,12,"Harry",[1,2]}
s[4]= 1,4

print(s)

#You can’t change its values — because tuples are immutable.