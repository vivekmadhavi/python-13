#wapp to generae the n-digit OTP

from random import *
txt="0123456789"

n=int(input("enter the value of n "))
if n >0:
	otp=""
	i = 1
	while i <=n:
		o = txt[randrange(len(txt))]
		otp=otp+o
		i = i+1
	print("otp", otp)
else:
	print("r u out of mind")