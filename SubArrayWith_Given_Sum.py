'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15

'''


'''

Algorithm:

Create three variables, i=1,l=0, sum = arr[0]
Traverse the array from start to end.
Update the variable sum by adding current element, sum = sum + array[i]
If the sum is greater than the given sum, update the variable sum as sum = sum – array[l], and update l as , l++.
If the sum is equal to given sum, print the subarray and break the loop.



'''

'''

# Returns true if the 
# there is a subarray 
# of arr[] with sum 
# equal to 'sum' 
# otherwise returns 
# false. Also, prints 
# the result 
def subArraySum(arr, n, sum): 
	
	# Pick a starting 
	# point 
	for i in range(n): 
		curr_sum = arr[i] 
	
		# try all subarrays 
		# starting with 'i' 
		j = i+1
		while j <= n: 
		
			if curr_sum == sum: 
				print ("Sum found between") 
				print("indexes %d and %d"%( i, j-1)) 
				
				return 1
				
			if curr_sum > sum or j == n: 
				break
			
			curr_sum = curr_sum + arr[j] 
			j += 1

	print ("No subarray found") 
	return 0

# Driver program 
arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 23

subArraySum(arr, n, sum) 

# This code is Contributed by shreyanshi_arun. 



'''
for _ in range(int(input())):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    sum1=arr[0]
    start=0
    i=1
    while(i<=n):

        while(sum1>s and start<i-1):

            sum1=sum1-arr[start]
            start+=1
        if(sum1==s):
            print(start+1,i)
            
            break
        if(i<n):
            sum1=sum1+arr[i]
        i+=1
    else:
        print(-1)
#space =O(1)
#time_complexity=O(n)