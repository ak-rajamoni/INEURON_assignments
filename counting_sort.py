# # Python program for counting sort 

# # The main function that sort the given string arr[] in 
# # alphabetical order 
# def countSort(arr): 

# 	# The output character array that will have sorted arr 
# 	output = [0 for i in range(256)] 

# 	# Create a count array to store count of inidividul 
# 	# characters and initialize count array as 0 
# 	count = [0 for i in range(256)] 

# 	# For storing the resulting answer since the 
# 	# string is immutable 
# 	ans = ["" for _ in arr] 

# 	# Store count of each character 
# 	for i in arr: 
# 		count[ord(i)] += 1
	
# 	print(count)
# 	# Change count[i] so that count[i] now contains actual 
# 	# position of this character in output array 
# 	for i in range(256): 
# 		count[i] += count[i-1] 

# 	print(count)

# 	# Build the output character array 
# 	for i in range(len(arr)): 
# 		output[count[ord(arr[i])]-1] = arr[i] 
# 		count[ord(arr[i])] -= 1

# 	# Copy the output array to arr, so that arr now 
# 	# contains sorted characters 
# 	for i in range(len(arr)): 
# 		ans[i] = output[i] 
# 	return ans 

# # Driver program to test above function 
# arr = "geeksforgeeks"
# ans = countSort(arr) 
# print("Sorted character array is %s" %ans) 

# # This code is contributed by Nikhil Kumar Singh 



 
def areRotations(string1, string2): 
	size1 = len(string1) 
	size2 = len(string2) 
	temp = '' 

	if size1 != size2: 
		return 0
	temp = string1 + string1 
	if (temp.count(string2)> 0): 
		return 1
	else: 
		return 0

# Driver program to test the above function 
string1 = "IndiaUSAEngland"
string2 = "USAEnglandIndia"

if areRotations(string1, string2): 
	print(True)
else: 
	print(False)

# This code is contributed by Bhavya Jain 
