#wapp to demo random module

from random import *

#randrange()->random integers
print(randrange(5))
print(randrange(7))
print(randrange(3,7))
print(randrange(2,10))
print(randrange(7,3,-1))

#random() -> random floating point number
print(random())


#randint() -> random integers
print(randint(2,5))

#choice() -> one random names from list
name=["sahil","vivek","bala","krish"]
print(choice(name))