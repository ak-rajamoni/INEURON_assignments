# def group_ana(words):
# 	arr=["".join(sorted(w)) for w in words]
# 	print(arr)
# 	d={}
# 	for i,e in enumerate(arr):
# 		d.setdefault(e,[]).append(i)
# 	print(d.values())
# 	for index in d.values():
# 		print([words[i] for i in index])

# group_ana(["bat","design","toc","cot","signed","tab"])

def minimum(arr):
	ts=0

	for i in range(len(arr)):
		s=0
		for j in range(len(arr)-i-1):
			if(arr[j]>arr[j+1]):
				(arr[j],arr[j+1])=(arr[j+1],arr[j])
				s+=1
				print(s)
		if(ts<s):
			ts=s
	return ts,arr

def mini(arr):
	ts=0
	s=0
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
			s+=1
		arr[j+1]=key
		print(arr,s)
		if(ts<s):
			ts=s


	return ts,arr


# print(minimum([5,1,3,2,7]))
# print(mini([5,1,3,2,7]))
print(mini([3,2,1]))



