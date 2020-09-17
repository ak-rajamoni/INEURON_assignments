'''
l,n=[6,2,3,1,7,8],6
print(n)
ind=l.index(n)
print(ind)
if n in l:
	ln=sorted(l)
	print(ln)
	ind1=ln.index(n)
	print(ind1)
	l[ind],l[ind1]=l[ind1],l[ind]
	print(l)
	print("swapped",''.join(map(str,ln)) if ln==l else print("not swapped"))
else:	
	print("Not swapped")

'''
def fil(last):
	return [x for x in last if x%2]
def d(n):
	return n%2==0


print(fil([1,2,3,4,5]))

def my_filter(func,sequence):
    res=[]
    for variable in sequence :
        if func(variable):
            res.append(variable)
    return res

def is_even(item):
    if item%2==0 :
        return True
    else :
        return False



seq=[1,2,3,4,5,6,7,8,9,10]
print(my_filter(is_even,seq))

print([item for item in seq if item])
