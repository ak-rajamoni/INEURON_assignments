# Python3 program to convert a tree 
# into its sum tree 

# Node defintion 
class node: 
	
	def __init__(self, data): 
		self.left = None
		self.right = None
		self.data = data 

# Convert a given tree to a tree where 
# every node contains sum of values of 
# nodes in left and right subtrees 
# in the original tree 
def toSumTree(Node) : 
	
	# Base case 
	if(Node == None) : 
		return 0
	

	# Store the old value 
	old_val = Node.data 

	# Recursively call for left and 
	# right subtrees and store the sum as 
	# new value of this node 
	# print("left",toSumTree(Node.right))

	Node.data = toSumTree(Node.left) +toSumTree(Node.right) 

	# Return the sum of values of nodes 
	# in left and right subtrees and 
	# old_value of this node 
	return Node.data + old_val 

# A utility function to print 
# inorder traversal of a Binary Tree 
def printInorder(Node) : 
	if (Node == None) : 
		return
	printInorder(Node.left) 
	print(Node.data, end = " ") 
	printInorder(Node.right) 
	
# Utility function to create a new Binary Tree node 
def newNode(data) : 
	temp = node(0) 
	temp.data = data 
	temp.left = None
	temp.right = None
	
	return temp 

# Driver Code 
if __name__ == "__main__": 
	root = None
	x = 0
	
	# Constructing tree given in the above figure 
	root = newNode(10) 
	root.left = newNode(20) 
	root.right = newNode(30) 
	root.left.left = newNode(40) 
	root.left.right = newNode(60) 
	# root.right.left = newNode(7) 
	# root.right.right = newNode(5) 
	
	toSumTree(root) 
	
	# Print inorder traversal of the converted 
	# tree to test result of toSumTree() 
	print("Inorder Traversal of the resultant tree is: ") 
	printInorder(root) 

# This code is contributed by Arnab Kundu 
