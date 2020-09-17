# n=100000111
# count=0
# for i in range(1,n+1):
	
# 	if n%i==0:
# 		count+=1
# print(count)
# if (count==2):
# 	print("prime number")
# else:
# 	print("composite number")

from math import *
n=10000011143242
bool_=True
rang=ceil(sqrt(n))+1
# print("n :rang",n,rang)
if n<1:
	bool_=False
if n==2:
	bool_=True
if n>2 and n%2==0:
	bool_=False
for i in range(3,rang,2):
	# print(n,i,n%i)
	if (n%i==0):
		bool_=False
# print(bool_)
if(bool_==True):
	print("prime")
else:
	print("composite")
