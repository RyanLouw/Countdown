from itertools import permutations
import enchant
d=enchant.Dict("en_US")
op = set ()
inp= "extreme" ##die moet 10 carakters wees.
# moet die string verander dat een letter nie in is nie.

letters= [x.lower() for x in inp]

##print(letters)
print ("hello world")

for n in range(3,len(inp)):
    for y in list (permutations(letters,n)):
        z="".join(y)
        if d.check(z):
           op.add(z)
print (op)