#wapp to generate random motivational msg


from random import *

msg=["do or die","live king size","live and let live","just do it","simon go back"]

#randrange()
print(msg[randrange(len(msg))])

#randint()

print(msg[randint(0,len(msg)-1)])


#choice
print(choice(msg))